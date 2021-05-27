from unittest.mock import Mock

from django.http import HttpRequest
from django.test import TestCase
from django.shortcuts import resolve_url as r
from eventex.core.admin import SpeakerModelAdmin, admin, TalkModelAdmin
from eventex.core.models import Speaker, Contact, Talk, Course


class ModelAdminTest(TestCase):
    def setUp(self):
        self.request = Mock()
        self.speaker = Speaker.objects.create(
            name="Grace Hopper",
            slug="grace-hopper",
            photo="http://hbn.link/hopper-pic",
            website="http://hbn.link/hopper-site",
            description="Programadora e almirante.",
        )
        self.speaker_model_admin = SpeakerModelAdmin(Speaker, admin.site)

    def test_speaker_admin_display_fields(self):
        fields = ["name", "photo_img", "website_link", "email", "phone"]
        for field in fields:
            with self.subTest():
                self.assertIn(field, self.speaker_model_admin.list_display)

    def test_website_link(self):
        self.assertEqual(
            self.speaker_model_admin.website_link(self.speaker),
            f'<a href="{self.speaker.website}">{self.speaker.website}</a>',
        )

    def test_photo_img(self):
        self.assertEqual(
            self.speaker_model_admin.photo_img(self.speaker),
            f'<img width="32px" src="{self.speaker.photo}" />',
        )

    def test_email(self):
        contact = Contact.objects.create(
            speaker=self.speaker, kind=Contact.EMAIL, value="zandor@leal.net"
        )
        self.assertEqual(self.speaker_model_admin.email(self.speaker).value, contact.value)

    def test_phone(self):
        contact = Contact.objects.create(
            speaker=self.speaker, kind=Contact.PHONE, value="21-999999999"
        )
        self.assertEqual(self.speaker_model_admin.phone(self.speaker).value, contact.value)

    def test_talk(self):
        talk = Talk.objects.create(title="Título da Palestra")
        c1 = Course.objects.create(
            title="Título do Curso",
            start="09:00",
            description="Descrição do curso.",
            slots=20,
        )
        talk_model_admin = TalkModelAdmin(Talk, admin.site)
        self.assertEqual(list(talk_model_admin.get_queryset(self.request)),
                         list(Talk.objects.filter(course=None)))
