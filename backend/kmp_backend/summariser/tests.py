from django.test import TestCase, Client
from django.urls import reverse
from unittest.mock import patch
import os

class GenerateSummaryTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('summariser')  # Adjust the URL name if different
        os.environ['GEMINI_API_KEY'] = 'fake_api_key_for_testing'  # Mock the API key for testing

    @patch('google.generativeai.GenerativeModel')
    def test_transcript_not_found(self, mock_model):
        response = self.client.post(self.url, {})
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.content.decode(), "Transcript not found")

def mock_response(text, feedback):
    class MockResponse:
        def __init__(self, text, feedback):
            self.text = text
            self.prompt_feedback = feedback
            self.finishReason = 'complete'

    return MockResponse(text, feedback)
