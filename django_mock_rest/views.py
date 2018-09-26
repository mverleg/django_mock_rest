from json import dumps
from time import sleep

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.views.decorators.http import require_GET

from django_mock_rest.config import is_enabled
from django_mock_rest.models import Endpoint
from django_mock_rest.search import match_paths, choose_response


@require_GET
@login_required
def django_mock_rest_api_index(request):
	if not is_enabled():
		return HttpResponse("Mock API not enabled", status=500)
	endpoints = Endpoint.objects.prefetch_related()
	index = tuple(endpoint.as_json() for endpoint in endpoints)
	return HttpResponse(
		content=dumps(index, indent=4),
		content_type='application/json'
	)


def django_mock_rest_api(request, path):
	if not is_enabled():
		return HttpResponse("Mock API not enabled", status=500)
	path = "/" + path + ("/" if not path.endswith("/") else "")
	# Filter by method
	endpoints = Endpoint.objects.filter(method=request.method)
	# Filter by path, regex-based
	matches = match_paths(endpoints, path)
	if len(matches) > 1:
		return HttpResponse("Configuration error: more than one match for this method & path", status=500)
	if len(matches) == 0:
		return HttpResponse("No such mock endpoint: {} {}".format(request.method, path), status=404)
	endpoint = matches[0]
	# Find a response
	response = choose_response(endpoint.responses.all())
	if response is None:
		return HttpResponse("Configuration error: no response with weight >0 configured for this endpoint", status=500)
	if response.is_timeout():
		print('Timeout response; waiting 61s')
		sleep(61)
	return response.as_http_response()
