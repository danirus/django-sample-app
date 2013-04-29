import mock

from django.core.urlresolvers import reverse
from django.template.loader import render_to_string
from django.test import TestCase as DjangoTestCase

from sample_app.conf import settings


class DiaryRedirectViewTestCase(DjangoTestCase):
    def test_redirects_when_diary_empty(self):
        response = self.client.get(reverse('diary'))
        self.assert_(response.status_code == 302)
        response = self.client.get(reverse('diary'), follow=True)
        self.assert_(response.content == render_to_string("home.html"))
