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

import datetime

from django.core.urlresolvers import reverse
from django.template.loader import render_to_string
from django.test import TestCase as DjangoTestCase

from sample_app.models import DiaryDay


class EmptyDiaryRedirectViewTestCase(DjangoTestCase):
    def test_redirects_when_diary_empty(self):
        ''''diary/' URL redirects when DiaryDay is empty.'''
        response = self.client.get(reverse('diary'))
        self.assert_(response.status_code == 302)
        response = self.client.get(reverse('diary'), follow=True)
        self.assertContains(response, render_to_string("home.html"), 
                            status_code=200)


class DiaryRedirectViewTestCase(DjangoTestCase):
    fixtures = ['testing_data']

    def test_redirects_to_most_recent_diaryday(self):
        ''''diary/' URL redirects to most recent Diary entry.'''
        response1 = self.client.get(reverse('diary'))
        self.assert_(response1.status_code == 302)
        response2 = self.client.get(reverse('diary'), follow=True)
        response3 = self.client.get(reverse(
                'diaryday', kwargs={'year': 1969, 'month': 'jul', 'day':20}))
        self.assert_(response2.content == response3.content)
        

class DiaryDayViewTestCase(DjangoTestCase):
    fixtures = ['testing_data']

    def test_get_context_data(self):
        '''DiaryDayView places the right data in the template context.'''
        response = self.client.get(
            reverse('diaryday', 
                    kwargs={'year': 1969, 'month': 'jul', 'day':20}))
        diaryday = DiaryDay.objects.get(pub_date=datetime.date(1969, 7, 20))
        for entry_a, entry_b in zip(response.context_data['entries'],
                                    diaryday.entries.all()):
            self.assert_(entry_a == entry_b)
        self.assertEqual(response.context_data['date'],
                         datetime.date(1969, 7, 20))
        self.assertEqual(response.context_data['previous_day'],
                         datetime.date(1959, 9, 13))
        self.assertEqual(response.context_data['next_day'], None)

    def test_get_object_raises_404_when_no_matching_diaryday(self):
        '''
        DiaryDayView raises 404 when requested date has no corresponding
        DiaryDay entry.
        '''
        response = self.client.get(
            reverse('diaryday', 
                    kwargs={'year': 1969, 'month': 'jul', 'day':21}))
        self.assert_(response.status_code == 404)

    def test_get_object_raises_404_when_malformed_url(self):
        '''DiaryDayView raises 404 when requested date has no valid format.'''
        response = self.client.get(
            reverse('diaryday', 
                    kwargs={'year': 1969, 'month': 'zzz', 'day':21}))
        self.assert_(response.status_code == 404)
        response = self.client.get(
            reverse('diaryday', 
                    kwargs={'year': 1969, 'month': 'jul', 'day':99}))
        self.assert_(response.status_code == 404)
