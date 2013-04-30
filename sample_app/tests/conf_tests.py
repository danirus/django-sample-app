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
        self.assert_(response.content == render_to_string("index.html"))
        
    @patch("sample_app.views.REDIRECT_TO_URL_NAME", new=None)
    def test_setting_to_none_redirects_to_root(self):
        '''Setting REDIRECT_TO_URL_NAME to None redirects to '/'.'''
        response = self.client.get(reverse('diary'), follow=True)
        self.assert_(response.content == render_to_string("index.html"))
