from django.test import SimpleTestCase
from django.urls import reverse


class SnacksTest(SimpleTestCase):

    def test_home_page_status_code(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_home_page_template(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'home.html')
        self.assertTemplateUsed(response, 'base.html')

    def test_about_page_status_code(self):
        url = reverse('about')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_about_page_template(self):
        url = reverse('about')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'about.html')

    def test_home_page_status_code500(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertNotEqual(response.status_code, 500)

    def test_about_page_status_code500(self):
        url = reverse('about')
        response = self.client.get(url)
        self.assertNotEqual(response.status_code, 500)

    def test_home_page_template_not_used_by_home(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertTemplateNotUsed(response, 'about.html')

    def test_home_page_template_not_used_by_about(self):
        url = reverse('about')
        response = self.client.get(url)
        self.assertTemplateNotUsed(response, 'home.html')
