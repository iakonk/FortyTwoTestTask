from django.core.urlresolvers import resolve
from django.test import TestCase
from apps.contact.views import contact
from django.http import HttpRequest


class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, contact)

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = contact(request)
        self.assertIn(b'Iana', response.content)
