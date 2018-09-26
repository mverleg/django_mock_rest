from django.conf import settings


def is_enabled():
	enabled = getattr(settings, 'DJANGO_MOCK_REST', None)
	if enabled is True:
		return True
	if enabled is False:
		return False
	if enabled is None:
		return settings.DEBUG
	raise Exception("Incorrect configuration - DJANGO_MOCK_REST must be True, False or None")
