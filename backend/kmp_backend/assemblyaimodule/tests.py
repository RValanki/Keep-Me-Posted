from django.test import TestCase, Client
from django.urls import reverse
from gtts import gTTS
from io import BytesIO
from . import assemblyAI_module as tai
from assemblyaimodule import views, models
from unittest.mock import patch, MagicMock
from rest_framework.response import Response
from rest_framework import status

class TranscribeTestCase(TestCase):
    # Setup API client to post requests for mocking
    def setUp(self):
        self.client = Client()
    
    # Test 1: Test transcribe() 
    @patch('assemblyaimodule.views.TS.transcribe')
    @patch('assemblyaimodule.views.AudioFileSerializer')
    @patch('assemblyaimodule.views.FileSystemStorage')
    def test_transcribe(self, MockTranscribe, MockSerializer, MockStorage):
        # Mock serializer object as valid
        mock_serializer = MockSerializer.return_value
        mock_serializer.is_valid.return_value = True
        mock_serializer.validated_data['audio_file'] = "test audio"
        mock_serializer.errors = "Error"

        # Mock uploaded file
        mock_storage = MockStorage.return_value
        mock_url = views.UPLOAD_DIRECTORY_PATH + "test"
        mock_storage.save.return_value = mock_url

        # Mock transcription tesult
        mock_transcribe = MockTranscribe.return_value
        mock_transcription_result = "I am testing, testing."
        mock_transcribe.return_value = mock_transcription_result
        mock_storage.delete = MagicMock(name='delete')

        # Mock a POST request
        mock_file = MagicMock()
        mock_file.data = "test data"
        response = self.client.post(reverse('transcribe'), {'audio_file': mock_file})

        print(f"Response status code: {response.status_code}")
        print(f"Response data: {response.data}")

        # Assert the response
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {'transcription': mock_transcription_result})

        # Assert frequency of all mock calls
        mock_serializer.assert_called_once_with(data={'audio_file': MagicMock()})
        mock_serializer.is_valid.assert_called_once()
        mock_storage.save.assert_called_once_with(mock_serializer.validated_data['audio_file'].name, mock_serializer.validated_data['audio_file'])
        MockTranscribe.assert_called_once_with(mock_url)
        mock_storage.delete.assert_called_once_with(mock_url)
