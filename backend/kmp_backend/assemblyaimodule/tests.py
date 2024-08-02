from django.test import TestCase
from gtts import gTTS
from io import BytesIO
from . import assemblyAI_module as tai
from . import views
import unittest
from unittest.mock import patch, Mock

class TranscribeTestCase(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()

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
    @patch('backend.kmp_backend.assemblyaimodule.views.TS.transcribe')
    @patch('backend.kmp_backend.assemblyaimodule.views.AudioFileSerializer')
    @patch('backend.kmp_backend.assemblyaimodule.views.FileSystemStorage')
    def test_transcribe(self, MockTranscribe, MockSerializer, MockStorage):
        # Mock serializer object as valid
        mock_serializer = MockSerializer.return_value
        mock_serializer.is_valid.return_value = True

        # Mock uploaded file
        mock_storage = MockStorage.return_value
        mock_url = views.UPLOAD_DIRECTORY_PATH + "test"
        mock_storage.save.return_value = mock_url

        # Mock transcription tesult
        mock_transcription_result = "I am testing, testing."
        MockTranscribe.return_value = mock_transcription_result

        
    # Test 1: Test return type of transcribe()
    def test_transcribe_type(self):
        test_text = "Hello, world."
        test_audio = self.generateAudio(test_text)
        self.assertIsInstance(tai.transcribe(test_audio), str)
    
    # Test 2: Test return type of transcribe_with_speakers
    def test_transcribe_speakers_type(self):
        test_text = "Hello, world."
        test_audio = self.generateAudio(test_text)
        self.assertIsInstance(tai.transcribe_with_speakers(test_audio), str)