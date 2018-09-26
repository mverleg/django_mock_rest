Django mock rest
===============================

Simple way to create static mock data at rest api endpoints in the Django admin.

If you're designing a rest api client, and want to create a simple mock server for testing, then this app lets you do that using the Django admin.

Install
===============================

* Install using

.. code:: bash

    pip install django-mock-rest

* Add `django_mock_rest` to installed apps in `settings.py`:

    INSTALLED_APPS = [
        ...
        'django_mock_rest',
        ...
    ]

* Add the root url to `url.py`:

    urlpatterns = [
        ...
	    url(r'^api-mock/', include('django_mock_rest.urls')),
        ...
    ]

How to use
===============================

In the Django admin, you can create endpoints:

.. image:: rources/admin_preview.png

After that, you can do http request to the endpoints you defined:

.. code:: bash

    $ curl -X GET http://127.0.0.1:8000/api-mock/post/1/
    {
        "post": "Hello world"
    }

You can also see an overview of all the mock endpoints (if logged in) by visiting `~`, i.e. `http://127.0.0.1:8000/api-mock/~`.
