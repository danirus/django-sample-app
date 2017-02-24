#-*- coding: utf-8 -*-

# django-sample-app - A Django app with setup, unittests, docs and demo
# Copyright (C) 2013,  Daniel Rus Morales

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import os
import sys
import unittest


def setup_django_settings():
    os.chdir(os.path.join(os.path.dirname(__file__), ".."))
    sys.path.insert(0, os.getcwd())
    os.environ["DJANGO_SETTINGS_MODULE"] = "tests.settings"


def run_tests():
    if not os.environ.get("DJANGO_SETTINGS_MODULE", False):
        setup_django_settings()

    import django
    from django.conf import settings
    from django.test.utils import get_runner

    django.setup()
    runner = get_runner(settings,"django.test.runner.DiscoverRunner")
    test_suite = runner(verbosity=2, interactive=True, failfast=False)
    return test_suite.run_tests(["sample_app"])
