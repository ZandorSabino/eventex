from django.test import TestCase


# Create your tests here.

class hometest(TestCase):

    def setup(self):
        self.response = self.client.get('/')

    def test_get(self):
        """GET / Must return status code 200"""
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        """Must use index.html"""
        self.assertTemplateUsed(self.response, 'index.html')
