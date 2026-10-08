from django.test import TestCase
from django.urls import reverse
from .models import Visitor

class GreetingTests(TestCase):
    def test_home(self):
        self.assertEqual(self.client.get(reverse('home')).status_code, 200)

    def test_name_saved_and_greeted(self):
        response = self.client.post(reverse('home'), {'name': 'Тимофей'})
        self.assertContains(response, 'Привет, Тимофей!')
        self.assertEqual(Visitor.objects.count(), 1)

    def test_empty_name_rejected(self):
        response = self.client.post(reverse('home'), {'name': '   '})
        self.assertEqual(Visitor.objects.count(), 0)
        self.assertContains(response, 'Обязательное поле')

    def test_html_is_escaped(self):
        response = self.client.post(reverse('home'), {'name': '<script>alert(1)</script>'})
        self.assertNotContains(response, '<script>alert(1)</script>', html=False)
