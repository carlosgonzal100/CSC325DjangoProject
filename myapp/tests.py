from django.test import TestCase
from django.urls import reverse, resolve

from myapp import views


class HomeViewTests(TestCase):

    def test_home_status_code(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_home_content(self):
        response = self.client.get(reverse('home'))
        self.assertContains(response, "Hello, World! This the home page of my django application")

    def test_home_url_uses_home_view(self):
        self.assertEqual(resolve('/').func, views.home)


class AboutViewTests(TestCase):

    def test_about_status_code(self):
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)

    def test_about_content(self):
        response = self.client.get(reverse('about'))
        self.assertContains(response, "About Page")
        self.assertContains(response, "This is Project is about Django")

    def test_about_url_uses_about_view(self):
        self.assertEqual(resolve('/about/').func, views.about)


class UnknownPageTests(TestCase):

    def test_unknown_page_returns_404(self):
        response = self.client.get('/this-page-does-not-exist/')
        self.assertEqual(response.status_code, 404)


class HelloApiTests(TestCase):

    def test_hello_api_status_code(self):
        response = self.client.get(reverse('hello_api'))
        self.assertEqual(response.status_code, 200)

    def test_hello_api_returns_json_message(self):
        response = self.client.get(reverse('hello_api'))
        self.assertEqual(response.json()["message"], "Hello from the CSC325 Django API")
        self.assertEqual(response.json()["course"], "CSC325")
