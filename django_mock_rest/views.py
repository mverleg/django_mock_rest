from django.http import HttpResponse

from django_mock_rest.models import Endpoint
from search import match_paths


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
	endpoint = matches[0]
	# Find a response
	
	
	return HttpResponse(path)
