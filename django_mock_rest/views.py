from django.http import HttpResponse


def django_mock_rest_api(request, path):
	return HttpResponse(path)
