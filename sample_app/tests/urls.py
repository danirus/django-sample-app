from django.conf import settings
from django.conf.urls.defaults import patterns, include, url


urlpatterns = patterns(
    'sample_app.tests.views',
    url(r'^diary/', include('sample_app.urls')),
    url(r'^home$', 'home', name='home'),
    url(r'^$', 'index', name='index'),
)
