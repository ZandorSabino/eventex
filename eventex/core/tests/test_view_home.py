from django.test import TestCase
from django.shortcuts import resolve_url as r

# Create your tests here.


class HomeTest(TestCase):
    fixtures = ["keynotes.json"]

    def setUp(self):
        self.response = self.client.get(r("home"))

    def test_get(self):
        """GET / Must return status code 200"""
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        """Must use index.html"""
        self.assertTemplateUsed(self.response, "index.html")

    def test_subscription_link(self):
        expected = 'href="{}"'.format(r("subscriptions:new"))
        self.assertContains(self.response, expected)

    def test_speakers(self):
        """Must show keynote speakers"""
        contents = [
            'href="{}"'.format(r("speaker_detail", slug="grace-hopper")),
            "Grace Hopper",
            "http://hbn.link/hopper-pic",
            'href="{}"'.format(r("speaker_detail", slug="alan-turing")),
            "Alan Turing",
            "http://hbn.link/turing-pic",
        ]
        for expected in contents:
            with self.subTest():
                self.assertContains(self.response, expected)

    def test_nav_have_links(self):
        contents = [
            'href="{}#overview"'.format(r("home")),
            'href="{}#sponsors"'.format(r("home")),
            'href="{}#speakers"'.format(r("home")),
            'href="{}#register"'.format(r("home")),
            'href="{}"'.format(r("talk_list")),
            'href="{}#venue"'.format(r("home")),
        ]
        for expected in contents:
            with self.subTest():
                self.assertContains(self.response, expected)
