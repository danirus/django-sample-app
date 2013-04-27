from django import VERSION as DJANGO_VERSION
if DJANGO_VERSION[0:2] < (1, 4):
    from django.conf.urls.defaults import patterns, url
else:
    from django.conf.urls import patterns, url

from sample_app.models import DiaryDay
from sample_app.views import DiaryDayView, DiaryRedirectView

urlpatterns = patterns('',
    url(r'^(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{1,2})/$',
        DiaryDayView.as_view(), name='diaryday'),

    url(r'^$', DiaryRedirectView.as_view(permanent=False), name='diary'),
)
