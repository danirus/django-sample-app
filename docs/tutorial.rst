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

The django-sample-app directory structure looks as follows::

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

The 3 root level directories separate the **docs**, the **demo project** and the actual **app's code**.  

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
   single: Docs

The docs directory
------------------

Use `sphinx <http://sphinx-doc.org/>`_ to initialize the content of this directory. Run the following command and answer the questions. Sphinx will create the necessary content to allow you to start writing your docs right away::

    $ cd docs/
    $ sphinx-quickstart


.. index::
   single: Demo
   pair: Demo, Project

The demo projects directory
---------------------------

Keep a two level structure here to allow several example projects live under the same directory. It is handy as well to hold media content and static files for the different demo projects.


.. index::
   single: Code
   pair: Code, Tests

The source code directory
-------------------------

The directory name and structure you create to hold your app's code is the same you have to use when you install your app in a Django project.
