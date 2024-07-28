from django.test import TestCase
from gtts import gTTS
import io
from .assemblyAI_module import transcribe, transcribe_with_speakers

class TranscribeTestCase(TestCase):
    # Helper function to generate audio files in memory
    def generateAudio(self, text: str, lang: str, accent: str):
        tts = gTTS(text, lang, accent)
        audio_file = io.BytesIO()
        tts.write_to_fp(audio_file)
        audio_file.seek(0)
        return audio_file
    
    # Test 1: Test if transcribe() can transcribe text from a basic audio file
    def test_transcribe_basic_text(self):
        test_text = "Hello, world."
        test_lang = "en"
        test_accent = "com.au"
        test_audio = self.generateAudio(text=test_text, lang=test_lang, tld=test_accent)
        self.assertEqual(test_text, transcribe(test_audio))
    
    # Helper function to generate audio with multiple speakers 
    def generateAudioMultipleSpeakers(self):
        # Generating lines of audio with speakers of Indian and South African accented English 
        line_one = self.generateAudio(text="This is a fascinating meeting that we are having today.", lang="en", tld="co.in")
        line_two = self.generateAudio(text="Truly a most fascinating meeting.", lang="en", tld="co.za")
        line_three = self.generateAudio(text="I have never in my life attended a more interesting meeting.", lang="en", tld="co.in")
        line_four = self.generateAudio(text="I never have and never will.", lang="en", tld="co.za")
        # Combining the lines of audio to create one audio file 
        combined_audio = line_one + line_two + line_three + line_four
        return combined_audio

    # Test 2: Test if transcribe_with_speakers() can transcribe text with speakers from a basic audio file 
    def test_transcribe_with_speakers(self):
        test_audio = self.generateAudioMultipleSpeakers()

        expected_result = (
            "Speaker 1: This is a fascinating meeting that we are having today.\n"
            "Speaker 2: Truly a most fascinating meeting.\n"
            "Speaker 1: I have never in my life attended a more interesting meeting.\n"
            "Speaker 2: I never have and never will.\n"
        )
        
        self.assertEqual(expected_result, transcribe_with_speakers(test_audio))
