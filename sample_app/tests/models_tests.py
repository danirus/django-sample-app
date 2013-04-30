from django.test import TestCase as DjangoTestCase

from sample_app.models import DiaryDay

class DiaryDayEntryTestCase(DjangoTestCase):
    fixtures = ['testing_data']

    def test_get_absolute_url(self):
        '''
        DiaryDayEntries' get_absolute_url points to corresponding DiaryDay's
        get_absolute_url.
        '''
        for day in DiaryDay.objects.all():
            for entry in day.entries.all():
                self.assertEqual(entry.get_absolute_url(),
                                 day.get_absolute_url())
