from django.contrib import admin
from django import forms

from django_mock_rest.models import Endpoint, Response


class ResponseInline(admin.StackedInline):
	model = Response
	fields = ('weight', 'status', 'data',)
	extra = 1


class EndpointAdminForm(forms.ModelForm):
	def clean(self):
		path = self.cleaned_data['path']
		if not path.startswith('/'):
			path = '/' + path
		if not path.endswith('/'):
			path = path + '/'
		self.cleaned_data['path'] = path
		return self.cleaned_data


class EndpointAdmin(admin.ModelAdmin):
	model = Endpoint
	fields = ('method', 'path', 'explanation', 'require_authentication',)
	# fields = ('method', 'path', 'parameters', 'explanation', 'require_authentication',)
	list_display = ('method', 'path_pattern', 'response_count',)
	list_display_links = list_display
	list_filter = ('method',)
	form = EndpointAdminForm
	inlines = [
		ResponseInline,
	]


admin.site.register(Endpoint, EndpointAdmin)
