from django.test import TestCase
from evento.core.forms import CoreForm


class CoreFormClass(TestCase):
    def test_form_has_fields(self):
        """Form must have 2 fields"""
        form = CoreForm()
        expected = ['aluno', 'professor']
        self.assertSequenceEqual(expected, list(form.fields))
