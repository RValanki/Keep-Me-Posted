from django.test import TestCase
from gtts import gTTS
from io import BytesIO
from .assemblyAI_module import transcribe, transcribe_with_speakers

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