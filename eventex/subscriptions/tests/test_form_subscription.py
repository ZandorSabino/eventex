from django.test import TestCase

from eventex.subscriptions.forms import SubscriptionForm


class SubscriptionFormTest(TestCase):
    def test_form_has_fields(self):
        """Form must have 4 fields"""
        form = SubscriptionForm()
        expected = ["name", "cpf", "email", "phone"]
        self.assertEqual(expected, list(form.fields))

    def test_cpf_is_digit(self):
        """CPF must only accept digits."""
        form = self.make_validated_form(cpf="ABCD5678901")
        self.assertFormErrorMessage(form, "cpf", "digits")

    def test_cpf_has_11_digits(self):
        """CPF must have 11 digits."""
        form = self.make_validated_form(cpf="1234")
        self.assertFormErrorMessage(form, "cpf", "length")

    def test_name_must_be_captalized(self):
        """Name must be capitalized"""
        form = self.make_validated_form(name="ZANDOR leal")
        self.assertEqual("Zandor Leal", form.cleaned_data["name"])

    def test_email_is_optional(self):
        """Email is optional"""
        form = self.make_validated_form(phone="")
        self.assertFalse(form.errors)

    def test_phone_is_optional(self):
        """Phone is optional"""
        form = self.make_validated_form(email="")
        self.assertFalse(form.errors)

    def test_must_informe_emaiil_or_phone(self):
        """Email and Phone are optional, but one must be informed."""
        form = self.make_validated_form(email="", phone="")
        self.assertEqual(["__all__"], list(form.errors))

    def assertFormErrorMessage(self, form, field, code):
        errors = form.errors.as_data()
        errors_list = errors[field]
        exception = errors_list[0]
        self.assertEqual(code, exception.code)

    def make_validated_form(self, **kwargs):
        valid = dict(
            name="Zandor Leal",
            cpf="12345678901",
            email="zandor@leal.com",
            phone="21-999999999",
        )
        data = dict(valid, **kwargs)
        form = SubscriptionForm(data)
        form.is_valid()
        return form
