from django.contrib import admin

from django_mock_rest.models import Endpoint, Response


class ResponseInline(admin.StackedInline):
	model = Response
	fields = ('weight', 'status', 'data',)
	extra = 1


class EndpointAdmin(admin.ModelAdmin):
	model = Endpoint
	fields = ('method', 'path', 'parameters', 'explanation', 'require_authentication',)
	list_display = ('method', 'path_pattern', 'response_count',)
	list_display_links = list_display
	list_filter = ('method',)
	inlines = [
		ResponseInline,
	]


admin.site.register(Endpoint, EndpointAdmin)
