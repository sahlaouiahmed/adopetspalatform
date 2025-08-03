from django.test import TestCase, Client
from django.urls import reverse


# Create your tests here.

############## PASS ###############

class AboutViewTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.url = reverse('about')

    def test_about_view_status_code(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'about_us/about.html')
