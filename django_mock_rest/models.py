import re
from collections import OrderedDict
from json import dumps

from django.db import models
from django.http import HttpResponse
from jsonfield import JSONField

# https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods
METHODS = (
	('GET', 'GET'),          # The GET method requests a representation of the specified resource. Requests using GET should only retrieve data.
	('HEAD', 'HEAD'),        # The HEAD method asks for a response identical to that of a GET request, but without the response body.
	('POST', 'POST'),        # The POST method is used to submit an entity to the specified resource, often causing a change in state or side effects on the server.
	('PUT', 'PUT'),          # The PUT method replaces all current representations of the target resource with the request payload.
	('PATCH', 'PATCH'),      # The PATCH method is used to apply partial modifications to a resource.
	('DELETE', 'DELETE'),    # The DELETE method deletes the specified resource.
	('CONNECT', 'CONNECT'),  # The CONNECT method establishes a tunnel to the server identified by the target resource.
	('OPTIONS', 'OPTIONS'),  # The OPTIONS method is used to describe the communication options for the target resource.
	('TRACE', 'TRACE'),      # The TRACE method performs a message loop-back test along the path to the target resource.
)


TIMEOUT = 504

# https://www.restapitutorial.com/httpstatuscodes.html
STATUSES = (
	(200, '200 OK'),
	(201, '201 Created'),
	(204, '204 No content'),
	(301, '301 Moved permanently'),
	(304, '304 Not modified'),
	(307, '307 Temporary redirect'),
	(400, '400 Bad request'),
	(401, '401 Unauthorized'),
	(403, '403 Forbidden'),
	(404, '404 Not found'),
	(409, '409 Conflict'),
	(500, '500 Internal server error'),
	(501, '501 Not implemented'),
	(TIMEOUT, 'Timeout (no response)'),
)


class Endpoint(models.Model):
	# Request
	method = models.CharField(max_length=8, choices=METHODS, default=METHODS[0][0])
	path = models.CharField(max_length=128, blank=False, null=False, help_text='The relative path of the url as a regular expression, i.e. /post/\d/')
	parameters = JSONField(blank=True, help_text='Enter request parameters as a json map')
	
	# Other
	require_authentication = models.BooleanField(default=False, null=False)
	explanation = models.TextField(blank=True, help_text='Describe this endpoint for other administrators of django-mock-rest')
	
	@property
	def response_count(self):
		return self.responses.count()
	
	@property
	def path_pattern(self):
		# return self.path.pattern
		return self.path
	
	@property
	def path_regex(self):
		return re.compile('^{}$'.format(self.path))
	
	def __str__(self):
		return '{} {}'.format(self.method, self.path)
	
	def as_json(self):
		return OrderedDict((
			('method', self.get_method_display()),
			('path', self.path),
			('parameters', self.parameters),
			('require_authentication', self.require_authentication),
			('responses', tuple(resp.as_json() for resp in self.responses.all())),
		))


class Response(models.Model):
	endpoint = models.ForeignKey(Endpoint, related_name='responses', on_delete=models.CASCADE)
	weight = models.PositiveIntegerField(default=1, help_text='The relative likelihood of this response being sent (0 is disabled)')
	status = models.PositiveSmallIntegerField(choices=STATUSES, default=STATUSES[0][0])
	data = JSONField(blank=True, help_text='Enter a static json response')
	
	def __str__(self):
		return '{} ({})'.format(self.get_status_display(), self.weight)
	
	def is_timeout(self):
		return self.status == TIMEOUT
	
	def as_http_response(self):
		return HttpResponse(
			content=dumps(self.data, indent=4),
			status=self.status,
			content_type='application/json'
		)
	
	def as_json(self):
		return OrderedDict((
			('weight', self.weight),
			('status', self.get_status_display()),
			('data', self.data),
		))
