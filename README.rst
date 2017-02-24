Django-sample-app
=================

Django-sample-app is a simple app that serves as an example of a generic reusable Django application. The actual code of the app implements a sample diary application with tests, demo project and documentation.

It runs under officially Django `supported versions <https://www.djangoproject.com/download/#supported-versions>`_:

* Django 1.8, Django 1.9 and Django 1.10
* Python 2.7 and Python 3 (3.2, 3.4, 3.5, 3.6)

This tutorial passes through all the steps to build the app, while the rest of the documentation addresses the sample diary.

Before reading this tutorial visit the official Django project website and read the tutorial on `how to write reusable apps <https://docs.djangoproject.com/en/1.5/intro/reusable-apps/>`_. This document serves as an extension.


Directory layout
================

Django-sample-app's directory structure looks as follows::

    django-sample-app/
    ├── docs
    ├── extra
    │   └── demo
    │       └── templates
    └── sample_app
        ├── conf
        ├── fixtures
        ├── templates
        │   └── sample_app
        └── tests
            └── templates

The 3 root level directories separate the **docs**, the **demo project** and the  **code**.  

The root level directory contains the following files::

    django-sample-app/
    ├── LICENSE
    ├── MANIFEST.in
    ├── AUTHORS
    ├── README.md
    ├── requirements.pip
    ├── requirements_tests.pip
    └── setup.py


The ``setup.py`` file
=====================

Additionally to the common setup content the ``setup.py`` file provides a hook to run the app's tests suite::

    ...
    from setuptools.command.test import test

    def run_tests(*args):
        from sample_app.tests import run_tests
        errors = run_tests()
        if errors:
            sys.exit(1)
        else:
            sys.exit(0)

    test.run_tests = run_tests

Which allows to run the tests with the test command argument::

    $ python setup.py test

Look at the code of the function ``run_tests`` defined in ``sample_app.tests.__init__.py`` to know the details on how Django gets setup to run the tests suite.


The docs directory
==================

Use `sphinx <http://sphinx-doc.org/>`_ to initialize the content of this directory. Run the following command and answer the questions. Sphinx will create the necessary content to allow you to start writing your docs right away::

    $ cd docs/
    $ sphinx-quickstart

To produce automatic documentation of your modules sphinx-build needs to reach out Django, your app's code and everything that happens to be imported in between. The ``conf.py`` file in ``django-sample-app/docs`` comes with code that activates the virtualenv in which the app has been developed. By activating the virtualenv in ``conf.py`` sphinx-build will reach out the modules. 

Adapt the code to point to the path of your ``bin/activate_this.py`` script in your virtualenv, or comment it out if you won't use it to avoid building errors. The code in ``conf.py`` that activate the virtualenv::

    ...
    import sys, os

    venv_path = os.path.abspath(os.path.join('..', '..'))
    activate_this = os.path.join(venv_path, 'bin/activate_this.py')
    execfile(activate_this, dict(__file__=activate_this))
    sys.path.insert(0, os.path.abspath(os.path.pardir))
    ...


Write the docs in reStructuredText (the Sphinx quick introduction to *rest*: `reStructuredText Primer <http://sphinx-doc.org/rest.html>`_), create as many rst files and directories as you need and then generate the documentation in HTML with::

    $ make html

You may also want to make the docs available, either in `Read the Docs <https://readthedocs.org/>`_, in `PyPI <http://pypi.python.org>`_, or in both. To feed theses services you will need a zip file with the generated html pages and the ``index.html`` file at the top level. *ReadtheDocs* automates the step by pulling the docs directly from the code repository.


The demo projects directory
===========================

The ``demo`` directory lives inside the ``extra`` directory. It can hang directly from the root, but the ``extra`` dir in front is handy to allow creation of additional example projects or temporary directories to hold static files or media without cluttering the root.

The demo directory contains a simple project to run the app in the simplest way possible. It should allow manual testing of all the app's functionalities, as it would be done in a UAT (User Acceptance Test) scenario.

The content::

    demo/
    ├── initial_data.json    -> user admin/admin and example data for the app
    ├── __init__.py
    ├── manage.py            
    ├── sample_app_demo.db   -> created by manage.py syncdb --noinput
    ├── settings.py
    ├── templates
    │   ├── base.html
    │   └── index.html
    ├── urls.py
    └── views.py


The ``manage.py`` file is like the regular Django project ``manage.py`` file with additional code to add both the ``sample_app`` parent directory and the demo project parent directory to the Python search path, and to create the ``DJANGO_SETTINGS_MODULE`` environment variable.

The ``initial_data.json`` file contains the minimum data to feed sample_app models and ``auth.User`` with an ``admin`` user.


Templates
---------

One of the goals of the demo project is to show in a glance how your application templates look like. 

The ``templates/`` directory of the demo project contains only templates that cover the views not covered by the sample application. This way developers can quickly have an idea of what are the explicit app's functionalities. Writing merely functional templates helps potential adopters to focus on what you get with the app. 

If you want to show extra use cases write extra demo sites, but provide at least one simple demo site with raw functionalities.


The source code directory
=========================

The name of the directory you create to hold the code of your app is the same name you have to add to your project's INSTALLED_APPS setting. The directory will contain an ``__init__.py`` to denote it is a Python package. In such file you can declare package wide constants like the version.  

App's source code directory layout::

    sample_app/
    ├── __init__.py
    ├── urls.py
    ├── models.py
    ├── views.py
    ├── admin.py
    ├── conf/
    │   ├── defaults.py
    │   └── __init__.py
    ├── fixtures/
    │   └── testing_data.json
    ├── templates/
    │   └── sample_app
    │       └── diaryday_detail.html
    └── tests/


App's structure is like any Django app. It's been adapted to be independent as explained in the official Django tutorial on writing reusable apps mentioned above.


App settings
------------

Depending on whether your app defines customizable settings you might need the ``conf/`` directory. Read first on `creating your own settings <https://docs.djangoproject.com/en/1.5/topics/settings/#creating-your-own-settings>`_ and on the `coding style regarding the use of Django settings <https://docs.djangoproject.com/en/1.5/internals/contributing/writing-code/coding-style/#use-of-django-conf-settings>`_. If your app finally comes with its own customizable site wide settings consider using the stuff in ``conf/`` or look for other full featured alternatives in `Django Packages <https://www.djangopackages.com/search/?q=settings>`_   

To define new settings using sample_app's ``conf/`` directory just declare them in the ``defaults.py`` module. The only one declared for the sample app is in use in the ``views.py`` module.


Fixtures
--------

Some apps load initial data on ``syncdb``. Should your app require it, the ``fixtures/`` directory is the place for it. Name the initial data file ``initial_data.json`` (.yml and .xml also supported) to load it automatically after your app's models get created.

Place data files related with app's tests here too. Later refer to them in your TestCases in the ``fixture`` class attribute::

   ...
   class DiaryRedirectViewTestCase(DjangoTestCase):
       fixtures = ['testing_data']
   ...


Tests
-----

An app is more reliable when it has tests covering as much code as possible. 

The minimum scaffolding necessary to run a Django app tests suite should load the settings module and the Django tests runner. You can also write less dependant tests suite `mocking Django <http://www.mattjmorrison.com/2011/09/mocking-django.html>`_ but I don't recommend it. Django is quite resourceful testing wise and using its facilities pays off the effort in terms of lines of code.

The ``tests/`` directory structure::

    tests/
    ├── __init__.py
    ├── settings.py
    ├── urls.py
    ├── conf_tests.py
    ├── models_tests.py
    ├── views.py
    ├── views_tests.py
    └── templates
        ├── home.html
        └── index.html


Tests suite
***********

The function ``run_tests``, called by the ``setup.py test`` command, does the following:

 1. Load the specific settings for the tests suite

 2. Get the tests runner (a Django specific runner that cleans up the database on every test case)

 3. Run the tests suite

The function ``run_tests``::

    def run_tests():
        if not os.environ.get("DJANGO_SETTINGS_MODULE", False):
            setup_django_settings()

        from django.conf import settings
        from django.test.utils import get_runner

        TestRunner = get_runner(settings)
        test_suite = TestRunner(verbosity=2, interactive=True, failfast=False)
        return test_suite.run_tests(["sample_app"])

The list passed as first argument to the function ``run_test`` (last call in the previous code) admits a variety of formatted strings:

 * ``app.TestClass.test_method``: Run a single specific test method.
 * ``app.TestClass``: Run all the test methods in a given class.
 * ``app``: Search for doctests and unittests in the named application.

When used with just the app's name Django looks for an attribute ``suite`` in the app's tests module to build the tests suite. You just have to build the tests suite and return it::

    def suite():
        if not os.environ.get("DJANGO_SETTINGS_MODULE", False):
            setup_django_settings()
        else:
            from django.conf import settings

        from sample_app.tests import conf_tests, models_tests, views_tests

        testsuite = unittest.TestSuite([
            unittest.TestLoader().loadTestsFromModule(conf_tests),
            unittest.TestLoader().loadTestsFromModule(models_tests),
            unittest.TestLoader().loadTestsFromModule(views_tests),
        ])
        return testsuite

Both, run_tests and suite, are part of the ``sample_app/tests/__init__.py`` module.
