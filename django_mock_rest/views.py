from time import sleep

from django.http import HttpResponse

from django_mock_rest.models import Endpoint
from django_mock_rest.search import match_paths, choose_response


def django_mock_rest_api(request, path):
	path = "/" + path
	# Filter by method
	endpoints = Endpoint.objects.filter(method=request.method)
	# Filter by path, regex-based
	matches = match_paths(endpoints, path)
	if len(matches) > 1:
		return HttpResponse("Configuration error: more than one match for this method & path", status=500)
	if len(matches) == 0:
		return HttpResponse("No such mock endpoint: {} {}".format(request.method, path), status=404)
	endpoint = matches[0][0]
	# Find a response
	response = choose_response(endpoint.responses.all())
	if response is None:
		return HttpResponse("Configuration error: no response with weight >0 configured for this endpoint", status=500)
	if response.is_timeout():
		print('Timeout response; waiting 61s')
		sleep(61)
	return response.to_http_response()
