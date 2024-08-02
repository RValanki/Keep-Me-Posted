from django.test import TestCase
from gtts import gTTS
from io import BytesIO
from .assemblyAI_module import transcribe, transcribe_with_speakers
import unittest
from unittest.mock import patch

class TranscribeTestCase(TestCase):
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
    
    # Test 1: Test transcribe() success
    @patch('aai.Transcriber')
    def test_transcribe_success(self, MockAssemblyAI):
        # Create a mock AssemblyAI instance and a mock transcript object
        mock_transcriber = MockAssemblyAI.return_value
        mock_transcript = MagicMock()

        # Set the transcript status and text for a successful transcription
        mock_transcript.status = aai.TranscriptStatus.success
        test_text = "Testing transcription function"
        mock_transcript.text = test_text
        mock_transcribe.transcribe.return_value = mock_transcript
        
        # Call transcribe with mocked transcript and assert
        result = transcribe('hello.mp3')
        self.assertEqual(result, test_text)

    # Test 1: Test return type of transcribe()
    def test_transcribe_type(self):
        test_text = "Hello, world."
        test_audio = self.generateAudio(test_text)
        self.assertIsInstance(transcribe(test_audio), str)
    
    # Test 2: Test return type of transcribe_with_speakers
    def test_transcribe_speakers_type(self):
        test_text = "Hello, world."
        test_audio = self.generateAudio(test_text)
        self.assertIsInstance(transcribe_with_speakers(test_audio), str)