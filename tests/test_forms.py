from django.test import TestCase, SimpleTestCase
from django.core.exceptions import ValidationError

from pulse_survey.survey import forms


# TODO - these tests should be changed if we add validation for Cabinet Office emails

class FeedbackFormTest(TestCase):
    def test_not_an_email(self):
        form = forms.FeedbackForm({"email": "not an email", "content": ""})
        form.is_valid()
        email_errors = form.errors["email"]
        self.assertTrue("Enter a valid email address" in str(email_errors))

    def test_incorrect_email(self):
        form = forms.FeedbackForm({"email": "test@example.com", "content": "some feedback"})
        form.is_valid()
        email_errors = form.errors["email"]
        self.assertTrue("Enter a Cabinet Office email address" in str(email_errors))

    def test_correct_email(self):
        form = forms.FeedbackForm({"email": "test@cabinetoffice.gov.uk", "content": "some feedback"})
        form.is_valid()
        no_email_errors = "email" not in form.errors
        self.assertTrue(no_email_errors)

class CabinetOfficeValidationTest(SimpleTestCase):
    def test_is_not_cabinet_office_email(self):
        invalid_email = "valid@example.com"
        with self.assertRaises(ValidationError) as e:
            forms.is_cabinet_office_email(invalid_email)
        self.assertEqual(e.exception.message, "Enter a Cabinet Office email address")

    def test_is_cabinet_office_email(self):
        valid_email = "valid@cabinetoffice.gov.uk"
        result = forms.is_cabinet_office_email(valid_email)
        self.assertTrue(result)


