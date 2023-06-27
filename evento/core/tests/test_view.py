from django.test import TestCase
from evento.core.forms import CoreForm

class HomeTest(TestCase):
    def setUp(self):
        self.resp = self.client.get('/')

    def test_template(self):
        """Must use index.html"""
        self.assertTemplateUsed(self.resp, 'index.html')

    def test_get(self):
        """Get / must return status code 200"""
        self.assertEqual(200, self.resp.status_code)

    def test_csrf(self):
        self.assertContains(self.resp, 'csrfmiddlewaretoken')

    def test_jas_form(self):
        form = self.resp.context['form']
        self.assertIsInstance(form, CoreForm)

    def test_html(self):
        """Html must contain a title, input and select tag"""
        tags = (('<h1', 1),
                ('<form', 1),
                ('<input', 3),
                ('type="text"', 1),
                ('type="submit"', 1),
                ('<select', 1),
                ('<option', 2)
                )
        for text, count in tags:
            with self.subTest():
                self.assertContains(self.resp, text, count)
