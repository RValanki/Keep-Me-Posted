from django.test import TestCase
from django.urls import reverse
from gtts import gTTS
from io import BytesIO
from . import assemblyAI_module as tai
from assemblyaimodule import views, models
import unittest
from unittest.mock import patch, MagicMock
from rest_framework.test import APIClient
from rest_framework.response import Response
from rest_framework import status

class TranscribeTestCase(TestCase):
    # Setup API client to post requests for mocking
    def setUp(self):
        self.client = APIClient()

    @staticmethod
    # Helper function to generate audio files in memory
    def generateAudio(text: str) -> BytesIO: 
        # Generates audio file
        tts = gTTS(text) 

        # Creates a file in memory and stores audio file content onto it
        audio_file = BytesIO()
        tts.write_to_fp(audio_file)
        audio_file.seek(0)

        return audio_file
    
    # Test 1: Test transcribe() 
    @patch('assemblyaimodule.views.TS.transcribe')
    @patch('assemblyaimodule.views.AudioFileSerializer')
    @patch('assemblyaimodule.views.FileSystemStorage')
    def test_transcribe(self, MockTranscribe, MockSerializer, MockStorage):
        # Mock serializer object as valid
        mock_serializer = MockSerializer.return_value
        mock_serializer.is_valid.return_value = True
        mock_serializer.validated_data = {'audio_file': MagicMock()}

        # Mock uploaded file
        mock_storage = MockStorage.return_value
        mock_url = views.UPLOAD_DIRECTORY_PATH + "test"
        mock_storage.save.return_value = mock_url

        # Mock transcription tesult
        mock_transcription_result = "I am testing, testing."
        MockTranscribe.return_value = mock_transcription_result

        # Create a mock audio file
        mock_file = BytesIO(b"fake audio data")
        mock_file.name = 'testfile.mp3'

        # Mock a POST request
        response = self.client.post(reverse('transcribe'), {'audio_file': mock_file}, format='multipart')

        # Assert the response
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {'transcription': mock_transcription_result})

        # Assert frequency of all mock calls
        MockAudioFileSerializer.assert_called_once_with(data={'audio_file': MagicMock()})
        mock_serializer.is_valid.assert_called_once()
        mock_fs.save.assert_called_once_with(mock_serializer.validated_data['audio_file'].name, mock_serializer.validated_data['audio_file'])
        MockTranscribe.assert_called_once_with(mock_saved_file_url)
        mock_fs.delete.assert_called_once_with(mock_saved_file_url)
