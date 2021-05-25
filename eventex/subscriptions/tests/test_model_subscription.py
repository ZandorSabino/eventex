from datetime import datetime

from django.test import TestCase
from eventex.subscriptions.models import Subscription
from django.shortcuts import resolve_url as r


class SubscriptionModelTest(TestCase):
    def setUp(self):
        self.obj = Subscription(
            name="Zandor Leal",
            cpf="12345678901",
            email="zandor@leal.com",
            phone="21-999999999",
        )
        self.obj.save()

    def test_create(self):
        self.assertTrue(Subscription.objects.exists())

    def test_created_at(self):
        """Subscription must have an auto created_at attr."""
        self.assertIsInstance(self.obj.created_at, datetime)

    def test_str(self):
        self.assertEqual("Zandor Leal", str(self.obj))

    def test_paid(self):
        self.assertEqual(False, self.obj.paid)

    def test_get_absolute_url(self):
        url = r("subscriptions:detail", self.obj.pk.int)
        self.assertEqual(url, self.obj.get_absolute_url())
