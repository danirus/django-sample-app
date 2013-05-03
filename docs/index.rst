.. django-sample-app documentation master file, created by
   sphinx-quickstart on Thu Apr 25 15:22:02 2013.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to django-sample-app's documentation!
=============================================

**django-sample-app** is a sample django application that provides a basic web Diary with the following features:

.. index::
   single: Features

1. An URL per day.
2. Each day in the diary may have several entries.
3. Entries in days will show up listed in its own day page.
4. Shows previous/next links to browse backwards/forwards only on days with actual entries.   
5. Diary management uses django's admin UI.

Run the demo project to see django-sample-app in action.

.. toctree::
   :maxdepth: 2

   example
   tutorial
   settings
   templates
   changelog

.. index::
   pair: Quick; Start

Quick start
===========

1. Edit the ``settings.py`` module and add ``sample_app`` to ``INSTALLED_APPS``::

    ...
    INSTALLED_APPS = (
        ...
        'sample_app',
    )

2. Edit the ``urls.py`` module and include django-sample-app's URLs::

    ...
    urlpatterns = patterns(
	...
	url(r'^diary/', include('sample_app.urls')),
        ...
    )

3. Create the database tables: ``python manage.py syncdb``

4. Run the development server and hit your app's URL!

Run the **demo** in ``django-sample-app/extra/demo`` to see an example.


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

