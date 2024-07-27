from django.test import TestCase
from gtts import gTTS
import io
from .assemblyAI_module import transcribe

class TranscribeTestCase(TestCase):
    # Helper function to generate audio files in memory
    def generateAudio(self, text: str):
        tts = gTTS(text)
        audio_file = io.BytesIO()
        tts.write_to_fp(audio_file)
        audio_file.seek(0)
        return audio_file
    
    # Test 1: Test if transcribe() can transcribe text from a basic audio file
    def test_transcribe_basic_text(self):
        test_text = "Hello, world."
        test_audio = self.generateAudio(test_text)
        self.assertEqual(test_text, transcribe(test_audio))