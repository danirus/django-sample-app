.. _ref-tutorial:

========
Tutorial
========

Django-sample-app is a simple app that serves as an example of a generic reusable Django application. The actual code of the app implements a sample diary application with tests, demo project and documentation.

This tutorial passes through all the steps to build the app, while the rest of the documentation addresses the sample diary.

Before reading this tutorial visit the official Django project website and read the tutorial on `how to write reusable apps <https://docs.djangoproject.com/en/1.5/intro/reusable-apps/>`_. This document serves as an extension.

.. index::
   single: Motivation

Directory layout
================

Django-sample-app's directory structure looks as follows::

    django-sample-app/
    ├── docs
    ├── extra
    │   └── demo
    │       └── templates
    └── sample_app
	├── conf
	├── fixtures
	├── templates
	│   └── sample_app
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


.. index::
   single: setup.py

The ``setup.py`` file
---------------------

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


.. index::
   single: Docs

The docs directory
------------------

Use `sphinx <http://sphinx-doc.org/>`_ to initialize the content of this directory. Run the following command and answer the questions. Sphinx will create the necessary content to allow you to start writing your docs right away::

    $ cd docs/
    $ sphinx-quickstart

Write the docs in reStructuredText (the Sphinx quick introduction to *rest*: `reStructuredText Primer <http://sphinx-doc.org/rest.html>`_) and generate the docs::

    $ make html

You may also want to make the docs available, either in `Read the Docs <https://readthedocs.org/>`_, in `PyPI <http://pypi.python.org>`_, or in both. To feed theses services you will need a zip file with the generated html pages and the ``index.html`` file at the top level. *ReadtheDocs* automates the step by pulling the docs directly from the code repository.


.. index::
   single: Demo
   pair: Demo, Project

The demo projects directory
---------------------------

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
    │   ├── base.html
    │   └── index.html
    ├── urls.py
    └── views.py


.. index::
   single: Code
   pair: Code, Tests

The source code directory
-------------------------

The directory name and structure you create to hold your app's code is the same you have to use when you install your app in a Django project.
