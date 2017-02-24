from django.test import TestCase as DjangoTestCase

from sample_app.utils import do_something


class TestDoSomething(DjangoTestCase):
    def test_do_something(self):
        self.assertEqual(do_something(), 10)

