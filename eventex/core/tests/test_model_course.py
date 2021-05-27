from django.test import TestCase

from eventex.core.managers import PeriodManager
from eventex.core.models import Course


class CourseModelTest(TestCase):
    def setUp(self):
        self.course = Course.objects.create(
            title="Título do Curso",
            start="09:00",
            description="Descrição do curso.",
            slots=20,
        )

    def test_create(self):
        self.assertTrue(Course.objects.exists())

    def test_speakers(self):
        """Course has many speakers and vice-versa"""
        self.course.speakers.create(
            name="Henrique Bastos",
            slug="henrique-bastos",
            website="http://henriquebastos.net",
        )
        self.assertEqual(1, self.course.speakers.count())

    def test_str(self):
        self.assertEqual("Título do Curso", str(self.course))

    def test_manager(self):
        self.assertIsInstance(Course.objects, PeriodManager)

    def test_ordering(self):
        self.assertListEqual(["start"], Course._meta.ordering)