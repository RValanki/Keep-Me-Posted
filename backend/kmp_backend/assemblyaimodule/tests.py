from django.test import TestCase
from gtts import gTTS
import io
from .assemblyAI_module import transcribe, transcribe_with_speakers

class TranscribeTestCase(TestCase):
    # Helper function to generate audio files in memory
    def generateAudio(self, text: str, tld: str, lang: str):
        tts = gTTS(text, tld, lang)
        audio_file = io.BytesIO()
        tts.write_to_fp(audio_file)
        audio_file.seek(0)
        return audio_file
    
    # Test 1: Test if transcribe() can transcribe text from a basic audio file
    def test_transcribe_basic_text(self):
        test_text = "Hello, world."
        test_lang = "en"
        test_accent = "com.au"
        test_audio = self.generateAudio(text=test_text, tld=test_accent, lang=test_lang)
        self.assertEqual(test_text, transcribe(test_audio))
    
    # Helper function to generate audio with multiple speakers 
    def generateAudioMultipleSpeakers(self, conversation: list[str]):
        transcript = []
        # Setting the language 
        test_lang = "en"
        for line_num in range(len(conversation)):
            # Setting and interchanging the accent 
            test_tld = "co.za"
            if line_num % 2 == 0:
                test_tld = "co.in"
            # Generating the conversation 
            line = gTTS(text=conversation[line_num], tld=test_tld, lang=test_lang)
            transcript.append(line)
        # Writing the conversation to an audio file 
        audio_file = io.BytesIO()
        for line in range(len(transcript)):
            transcript[line].write_to_fp(audio_file)
        audio_file.seek(0)
        return audio_file


    # Test 2: Test if transcribe_with_speakers() can transcribe text with speakers from a basic audio file 
    def test_transcribe_with_speakers(self):
        test_audio = self.generateAudioMultipleSpeakers([
            "This is a fascinating meeting that we are having today.", 
            "Truly a most fascinating meeting.",  
            "I have never in my life attended a more interesting meeting.", 
            "I never have and never will."
        ])

        expected_result = (
            "Speaker A: This is a fascinating meeting that we are having today.\n" + 
            "Speaker B: Truly a most fascinating meeting.\n" + 
            "Speaker A: I have never in my life attended a more interesting meeting.\n" + 
            "Speaker B: I never have and never will.\n"
        )
        
        self.assertEqual(expected_result, transcribe_with_speakers(test_audio))
