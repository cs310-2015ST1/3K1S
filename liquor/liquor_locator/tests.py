from django.test import TestCase
from django.utils import timezone


# Create your tests here.
class timezoneTestCase(TestCase):
	def test_timezone(self):
		tz = timezone.now()
		self.assertEqual(str(tz.tzinfo), "UTC")
