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
import shutil
import sys
import unittest


def setup_django_settings():
    os.chdir(os.path.join(os.path.dirname(__file__), ".."))
    sys.path.insert(0, os.getcwd())
    os.environ["DJANGO_SETTINGS_MODULE"] = "tests.settings"


def run_tests():
    if not os.environ.get("DJANGO_SETTINGS_MODULE", False):
        setup_django_settings()

    from django.conf import settings
    from django.test.utils import get_runner

    TestRunner = get_runner(settings)
    test_suite = TestRunner(verbosity=2, interactive=True, failfast=False)
    return test_suite.run_tests(["sample_app"])
    

def suite():
    if not os.environ.get("DJANGO_SETTINGS_MODULE", False):
        setup_django_settings()
    else:
        from django.conf import settings

    from sample_app.tests import (conf_tests, models_tests, views_tests,
                                  utils_tests)

    testsuite = unittest.TestSuite([
        unittest.TestLoader().loadTestsFromModule(conf_tests),
        unittest.TestLoader().loadTestsFromModule(models_tests),
        unittest.TestLoader().loadTestsFromModule(views_tests),
        unittest.TestLoader().loadTestsFromModule(utils_tests),
    ])
    return testsuite


if __name__ == "__main__":
    run_tests()
