from django.conf.urls import url

from django_mock_rest.views import django_mock_rest_api

urlpatterns = [
	url(r'^(?P<path>[\w\-+/]*)$', django_mock_rest_api, name='django_mock_rest'),
]
