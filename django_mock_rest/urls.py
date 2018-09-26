from django.conf.urls import url

from django_mock_rest.views import django_mock_rest_api, django_mock_rest_api_index

urlpatterns = [
	url(r'^~$', django_mock_rest_api_index, name='django_mock_rest_index'),
	url(r'^(?P<path>[\w\-+/]*)$', django_mock_rest_api, name='django_mock_rest'),
]
