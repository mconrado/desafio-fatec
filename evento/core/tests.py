from django.test import TestCase


class HomeTest(TestCase):

    def test_template(self):
        """Must use index.html"""
        self.assertTemplateUsed(self.client.get('/'), 'index.html')

    def test_get(self):
        """Get / must return status code 200"""
        self.assertEqual(200, self.client.get('/').status_code)

    def test_html(self):
        """Html must contain a title, input and select tag"""
        tags = (('<h1', 1),
                ('<form', 1),
                ('<input', 2),
                ('type="text"', 1),
                ('type="submit"', 1),
                ('<select', 1),
                ('<option', 2)
                )
        for text, count in tags:
            with self.subTest():
                self.assertContains(self.client.get('/'), text, count)
