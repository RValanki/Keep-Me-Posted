from django.test import TestCase, Client
from django.urls import reverse
from unittest.mock import patch
import os

class GenerateSummaryTests(TestCase):
    # Set up method that runs before every test method
    def setUp(self):
        self.client = Client()
        # Get the URL for the summarizer view by its name
        self.url = reverse('summariser')
        # Mock the API key for testing
        os.environ['GEMINI_API_KEY'] = 'fake_api_key_for_testing'

    #pretend generative model works
    @patch('google.generativeai.GenerativeModel')
    def test_transcript_not_found(self, mock_model):
        response = self.client.post(self.url, {})
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.content.decode(), "Transcript not found")

    @patch('google.generativeai.GenerativeModel')
    def test_safe_transcript(self, mock_model):
        mock_model_instance = mock_model.return_value
        mock_model_instance.generate_content.return_value = mock_response("This is a safe summary.", {})

        response = self.client.post(self.url, {'transcript': 'This is a test transcript.'})
        self.assertEqual(response.status_code, 200)
        self.assertIn('summary', response.json())
        self.assertEqual(response.json()['summary'], "This is a safe summary.")

    @patch('google.generativeai.GenerativeModel')
    def test_transcript_with_swear_word(self, mock_model):
        mock_model_instance = mock_model.return_value
        mock_model_instance.generate_content.return_value = mock_response("This transcript contains inappropriate content.", {"blockReason": "Hate Speech"})

        response = self.client.post(self.url, {'transcript': 'This is a damn test transcript.'})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.content.decode(), "Unsafe transcript provided")


def mock_response(text, feedback):
    class MockResponse:
        def __init__(self, text, feedback):
            self.text = text
            self.prompt_feedback = feedback
            self.finishReason = 'complete'

    return MockResponse(text, feedback)
