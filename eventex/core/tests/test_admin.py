from django.test import TestCase
from django.shortcuts import resolve_url as r
from eventex.core.admin import SpeakerModelAdmin, admin
from eventex.core.models import Speaker, Contact


class SpeakerModelAdminTest(TestCase):
    def setUp(self):
        self.speaker = Speaker.objects.create(
            name="Grace Hopper",
            slug="grace-hopper",
            photo="http://hbn.link/hopper-pic",
            website="http://hbn.link/hopper-site",
            description="Programadora e almirante.",
        )
        self.model_admin = SpeakerModelAdmin(Speaker, admin.site)

    def test_speaker_admin_display_fields(self):
        fields = ["name",
                  "photo_img",
                  "website_link",
                  "email",
                  "phone"]
        for field in fields:
            with self.subTest():
                self.assertIn(field, self.model_admin.list_display)

    def test_website_link(self):
        self.assertEqual(self.model_admin.website_link(self.speaker),
                         f'<a href="{self.speaker.website}">{self.speaker.website}</a>')

    def test_photo_img(self):
        self.assertEqual(self.model_admin.photo_img(self.speaker),
                         f'<img width="32px" src="{self.speaker.photo}" />')