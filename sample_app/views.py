#-*- coding: utf-8 -*-

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
