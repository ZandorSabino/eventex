from django.test import TestCase
from eventex.subscriptions.forms import SubscriptionForm

class SubscribeTest(TestCase):

    def setUp(self):
        self.resp = self.client.get('/inscricao/')
        self.form = self.resp.context['form']

    def test_get(self):
        """Get / must /inscricao/ must return status code 200"""
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        """Must use subscriptions/subscription_form.html"""
        self.assertTemplateUsed(self.resp, 'subscriptions/subscription_form.html')

    def test_html(self):
        """Html must contain input tags"""
        self.assertContains(self.resp, '<form')
        self.assertContains(self.resp, '<input', 6)
        self.assertContains(self.resp, 'type="text"', 3)
        self.assertContains(self.resp, 'type="email"')
        self.assertContains(self.resp, 'type="submit"')

    def test_csrf(self):
        """Html must contain csrf"""
        self.assertContains(self.resp, 'csrfmiddlewaretoken')

    def test_has_form(self):
        """Contex must have subscription form"""

        self.assertIsInstance(self.form, SubscriptionForm)

    def test_form_has_fields(self):
        """Form must have 4 fields"""
        self.assertEqual(['name', 'cpf', 'email', 'phone'], list(self.form.fields))
