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

try:
    from unittest.mock import patch
except ImportError:
    from mock import patch

from django.core.urlresolvers import reverse
from django.template.loader import render_to_string
from django.test import TestCase as DjangoTestCase

from sample_app.conf import settings
from sample_app.models import DiaryDay


class RedirectToURLNameSettingTestCase(DjangoTestCase):
    @patch("sample_app.views.REDIRECT_TO_URL_NAME", new="index")
    def test_setting_to_a_specific_named_url(self):
        '''Changing setting REDIRECT_TO_URL_NAME changes redirection target.'''
        response = self.client.get(reverse('diary'), follow=True)
        self.assertContains(response, render_to_string("index.html"),
                            status_code=200)
        
    @patch("sample_app.views.REDIRECT_TO_URL_NAME", new=None)
    def test_setting_to_none_redirects_to_root(self):
        '''Setting REDIRECT_TO_URL_NAME to None redirects to '/'.'''
        response = self.client.get(reverse('diary'), follow=True)
        self.assertContains(response, render_to_string("index.html"),
                            status_code=200)
