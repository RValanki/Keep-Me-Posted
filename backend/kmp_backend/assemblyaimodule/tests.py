from django.test import TestCase
from gtts import gTTS
from io import BytesIO
from . import assemblyAI_module as tai
import unittest
from unittest.mock import patch, Mock

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
    
    # Test 1: Test transcribe() (AssemblyAI)
    @patch('backend.kmp_backend.assemblyaimodule.assemblyAI_module.aai.Transcriber')
    @patch('backend.kmp_backend.assemblyaimodule.assemblyAI_module.aai.TranscriptStatus')
    def test_transcribe_success(self, MockTranscriber, MockTranscriptStatus):
        # Create a mock AssemblyAI instance and a mock transcript and transcriptstatus object
        mock_transcriber = MockTranscriber.return_value
        mock_transcript = Mock()
        MockTranscriptStatus.success = 's'
        MockTranscriptStatus.error = 'e'

        # Set the transcript status and text for a successful transcription
        mock_transcript.status = MockTranscriptStatus.success
        test_text = "Testing transcription function"    
        mock_transcript.text = test_text
        mock_transcriber.transcribe.return_value = mock_transcript

        print("Mock Transcript Status:", mock_transcript.status)
        print("Mock Transcript Text:", mock_transcript.text)
        
        # Call transcribe with mocked transcript and assert
        result = tai.transcribe("test")
        print("Transcribe Result:", result)
        self.assertEqual(result, test_text)

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