from django.test import TestCase

# Create your tests here.
class ApiTests(TestCase):
    def test_fail(self):
        self.assertTrue(False)
        self.assertEqual(True, False)
