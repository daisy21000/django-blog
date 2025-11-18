from django.test import TestCase
from .forms import CollaborateForm


class TestCollaborateForm(TestCase):

    def test_form_is_valid(self):
        """ Test for all fields"""
        form = CollaborateForm({
            'name': 'hi',
            'email': 'test@test.com',
            'message': 'Hello!'
        })
        self.assertTrue(form.is_valid(), msg="Form is not valid")

    def test_form_is_invalid_without_name(self):
        form = CollaborateForm({
            'name': '',
            'email': 'test@test.com',
            'message': 'Hello!'
        })
        self.assertFalse(form.is_valid(), msg="Form is valid without a name")

    def test_form_is_invalid_without_email(self):
        form = CollaborateForm({
            'name': 'hi',
            'email': '',
            'message': 'Hello!'
        })
        self.assertFalse(form.is_valid(), msg="Form is valid without an email")

    def test_form_is_invalid_without_message(self):
        form = CollaborateForm({
            'name': 'hi',
            'email': 'test@test.com',
            'message': ''
        })
        self.assertFalse(form.is_valid(), msg="Form is valid without a message")
