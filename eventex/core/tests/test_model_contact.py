from django.core.exceptions import ValidationError
from django.test import TestCase
from eventex.core.models import Speaker, Contact


class ContactModelTest(TestCase):
    def setUp(self):
        self.speaker = Speaker.objects.create(
            name="Zandor Leal", slug="zandor-leal", photo="http://zsl.link/zl-pic"
        )

    def test_email(self):
        contact = Contact.objects.create(
            speaker=self.speaker, kind=Contact.EMAIL, value="zandor@leal.net"
        )
        self.assertTrue(Contact.objects.exists())

    def test_phone(self):
        contact = Contact.objects.create(
            speaker=self.speaker, kind=Contact.PHONE, value="21-999999999"
        )
        self.assertTrue(Contact.objects.exists())

    def test_choices(self):
        """Contact kind should be limited to E or P"""
        contact = Contact(speaker=self.speaker, kind="A", value="B")
        self.assertRaises(ValidationError, contact.full_clean)

    def test_str(self):
        contact = Contact(
            speaker=self.speaker, kind=Contact.PHONE, value="21-999999999"
        )
        self.assertEqual("21-999999999", str(contact))


class ContactManagerTest(TestCase):
    def setUp(self):
        s = Speaker.objects.create(
            name="Henrique Bastos",
            slug="henrique-bastos",
            photo="http://hbn.link/hb-píc",
        )

        s.contact_set.create(kind=Contact.EMAIL, value="henrique@bastos.net")
        s.contact_set.create(kind=Contact.PHONE, value="21-996186180")

    def test_emails(self):
        qs = Contact.objects.emails()
        expected = ["henrique@bastos.net"]
        self.assertQuerysetEqual(qs, expected, lambda o: o.value)

    def test_phones(self):
        qs = Contact.objects.phones()
        expected = ["21-996186180"]
        self.assertQuerysetEqual(qs, expected, lambda o: o.value)
