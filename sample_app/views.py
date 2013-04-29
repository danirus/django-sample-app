#-*- coding: utf-8 -*-

import datetime

from django.core.urlresolvers import reverse
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
                            " format '%(date_format)'") 
                          % {'date_string': date_string, 
                             'date_format': date_format})

    def get_context_data(self, **kwargs):
        context = super(DiaryDayView, self).get_context_data(**kwargs)
        qs = self.object.entries.all()
        context.update({
            'entries': qs,
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
