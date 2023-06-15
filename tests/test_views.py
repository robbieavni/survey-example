import uuid
from django.test import TestCase


class TestViews(TestCase):
    def test_index(self):
        response = self.client.get("")
        self.assertEqual(response.status_code, 200)
    
    def test_location_page(self):
        session_id = uuid.uuid4()
        response = self.client.get(f"/survey/{session_id}/location-question/")
        self.assertEqual(response.status_code, 200)

class EmailFormViewTests(TestCase):
    def test_valid_email(self):
        form_data = {"email": "test@cabinetoffice.gov.uk", "content": "Test", "next": "Submit feedback"}
        response = self.client.post("/survey/feedback/", data=form_data)
        self.assertRedirects(response, '/survey/end/', status_code=302)

    def test_invalid_email(self):
        form_data = {"email": "test@gmail.com", "content": "Test", "next": "Submit feedback"}
        response = self.client.post("/survey/feedback/", data=form_data)
        self.assertIn(b"Enter a Cabinet Office email address", response.content)
        self.assertEqual(response.status_code, 200)