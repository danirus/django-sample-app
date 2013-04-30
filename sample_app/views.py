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
from django.http import Http404
from django.utils.translation import ugettext as _
from django.views.generic import RedirectView
from django.views.generic.dates import DateDetailView

from sample_app.conf import settings
from sample_app.models import DiaryDay, DiaryDayEntry


REDIRECT_TO_URL_NAME = getattr(settings, 'SAMPLE_APP_REDIRECT_TO_URL_NAME', None)


class DiaryDayView(DateDetailView):
    model = DiaryDay
    date_field = "pub_date"
    month_format = "%b"
    allow_future = True

    def get_allow_empty(self):
        return False

    def get_object(self, queryset=None):
        year_v, year_f = self.get_year(), self.get_year_format()
        month_v, month_f = self.get_month(), self.get_month_format()
        day_v, day_f = self.get_day(), self.get_day_format()
        date_format = "__".join((year_f, month_f, day_f))
        date_string = "__".join((year_v, month_v, day_v))
        try:
            self.date = datetime.datetime.strptime(date_string, 
                                                   date_format).date()
            return DiaryDay.objects.get(pub_date=self.date)
        except ValueError:
            raise Http404(_("Invalid date string '%(date_string)s' given"
                            " format '%(date_format)s'") 
                          % {'date_string': date_string, 
                             'date_format': date_format})
        except DiaryDay.DoesNotExist:
            raise Http404(_("DiaryDay doesn't exist"))

    def get_context_data(self, **kwargs):
        context = super(DiaryDayView, self).get_context_data(**kwargs)
        qs = self.object.entries.all()
        context.update({
            'entries': qs,
            'date': self.date,
            'previous_day': self.get_previous_day(self.date),
            'next_day': self.get_next_day(self.date),
        })
        return context


class DiaryRedirectView(RedirectView):
    def get_redirect_url(self, **kwargs):
        diarydays = DiaryDay.objects.all().order_by("-pub_date")
        if len(diarydays) == 0:
            if REDIRECT_TO_URL_NAME:
                return reverse(REDIRECT_TO_URL_NAME)
            else:
                return '/'
        else:
            return diarydays[0].get_absolute_url()
