# -*- coding: utf-8 -*-

from setuptools import setup

with open('README.rst', 'r') as fh:
	readme = fh.read()

setup(
	name='django-mock-rest',
	description='Simple way to create static mock data at rest api endpoints in the Django admin',
	long_description=readme,
	url='https://github.com/mverleg/django_mock_rest',
	author='Mark V',
	maintainer='(the author)',
	author_email='mverleg.noreply@gmail.com',
	license='Revised BSD License (LICENSE.txt)',
	keywords=['django', 'mock', 'test', 'unit-test', 'django-admin', 'rest', 'rest-api', 'api', 'http'],
	version='1.0',
	packages=['django_mock_rest', 'django_mock_rest.migrations',],
	include_package_data=True,
	zip_safe=True,
	classifiers=[
		'Development Status :: 5 - Production/Stable',
		'Intended Audience :: Developers',
		'Natural Language :: English',
		'License :: OSI Approved :: BSD License',
		'Operating System :: OS Independent',
		'Programming Language :: Python',
		'Programming Language :: Python :: 3',
		'Programming Language :: Python :: 3.4',
		'Programming Language :: Python :: 3.5',
		'Programming Language :: Python :: 3.6',
		'Programming Language :: Python :: 3.7',
		'Topic :: Software Development :: Libraries :: Python Modules',
	],
	install_requires= [
		'django>=2.0',
		'django-regex-field>=1.2',
		'jsonfield>=2.0',
	]
)
