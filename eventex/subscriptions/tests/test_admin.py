import unittest
from unittest.mock import Mock

from django.test import TestCase
from eventex.subscriptions.admin import SubscriptionModelAdmin, Subscription, admin


class SubscriptionModelAdminTest(TestCase):
    def setUp(self):
        self.obj = Subscription.objects.create(
            name="Zandor Sabino",
            cpf="12345678901",
            email="zandor@sabino.net",
            phone="21-999999999",
        )
        self.model_admin = SubscriptionModelAdmin(Subscription, admin.site)

    def test_has_action(self):
        """Action mark_as_paid should be instaled."""
        self.assertIn("mark_as_paid", self.model_admin.actions)

    def test_mark_all(self):
        """It should mark all selected subscriptions as paid."""
        self.call_action()
        self.assertEqual(1, Subscription.objects.filter(paid=True).count())

    def test_message_one_object(self):
        """It should sen a message to user."""
        mock = self.call_action()
        mock.assert_called_once_with(None, "1 inscrição foi marcada como paga.")

    def test_message_many_object(self):
        """It should sen a message to user."""
        Subscription(
            name="Sabino Zandor",
            cpf="10987654321",
            email="sabino@zandor.net",
            phone="21-999999988",
        ).save()
        mock = self.call_action()
        mock.assert_called_once_with(None, "2 inscrições foram marcadas como pagas.")

    def call_action(self):
        queryset = Subscription.objects.all()

        mock = Mock()
        old_message_user = SubscriptionModelAdmin.message_user
        SubscriptionModelAdmin.message_user = mock

        self.model_admin.mark_as_paid(None, queryset)

        SubscriptionModelAdmin.message_user = old_message_user

        return mock

    def test_subscribed_today(self):
        self.assertTrue(SubscriptionModelAdmin.subscribed_today(self, self.obj), '')
