from django.test import TestCase
from .assemblyAI_module import transcribe, transcribe_with_speakers
from io import BytesIO
from gtts import gTTS
from google.cloud import texttospeech
import soundfile as sf
import librosa
import numpy as np
import os
from dotenv import load_dotenv
import pyworld as pw   

load_dotenv()
google_credentials_path = os.getenv('GOOGLE_APPLICATION_CREDENTIALS')
class TranscribeTestCase(TestCase):
    # Helper function to generate a text-to-speech audio file in memory
    def generateAudio(self, text: str, voice_name: str, language: str):
        # Declares text to speech API client
        APIclient = texttospeech.TextToSpeechClient()

        # Configures the speaker voice and language
        voice = texttospeech.VoiceSelectionParams(
            language_code = language,
            name = voice_name
        )

        # Configures properties for response
        response = APIclient.synthesize_speech(
            input = texttospeech.SynthesisInput(text = text), 
            voice = voice, 
            audio_config = texttospeech.AudioConfig(audio_encoding = texttospeech.AudioEncoding.LINEAR16)
        )
        
        # Stores created audio into a file in memory
        audio_data = response.audio_content
        audio_file = BytesIO(audio_data)
        audio_file.seek(0)

        # Reads the audio file to extract audio content and sample rate
        data, samplerate = sf.read(audio_file)

        return data, samplerate
    
    # Combines generated audio into one conversations
    def generateAudioMultiSpeaker(self, texts: list[str], speakers: list[str], languages: list[str]):
        # Declares a np array of floating 32 bit numbers to store audio content
        data = np.array([], dtype = np.float32)

        # Generates individual sentence audio and concatenates them, with silence
        for text, speaker, language in zip(texts, speakers, languages):
            audio, sample_rate = self.generateAudio(text, speaker, language)
            silence = np.zeros(int(1 * sample_rate))  # 0.5 seconds of silence
            data = np.concatenate((data, audio, silence))

        return data, sample_rate
    
    # Recombines audio content and sample rate into a soundfile in memory, ready to be used
    def generateAudioFile(self, audio_data, sample_rate: int):
        # Converts audio content + sample rate into a wave file
        audio_file = BytesIO()
        with sf.SoundFile(audio_file, 'w', samplerate=sample_rate, channels=1, format='WAV') as file:
            file.write(audio_data)
        audio_file.seek(0)

        return audio_file
    
    # Test 1: Test if transcribe() can transcribe text from a basic audio file
    def test_transcribe_basic_text(self):
        test_text = "Hello, world. My name is John Smith, and I am 25 years old."
        test_lang = "en-US"
        test_voice = "en-US-Standard-A"
        test_audio, sample_rate = self.generateAudio(test_text, test_voice, test_lang);
        test_audio_file = self.generateAudioFile(test_audio, sample_rate)
        self.assertEqual(test_text, transcribe(test_audio_file))

    # Test 2: Test if transcribe_with_speakers() can transcribe text with speakers from a basic audio file 
    def test_transcribe_with_speakers(self):
        test_text = [
            "This is a fascinating meeting that we are having today.", 
            "I have never in my life attended a more interesting meeting.",
        ]
        test_lang = ["en-US",  "en-US"]
        test_voices = ["en-US-Standard-A", "en-IN-Standard-A"]
        test_audio, sample_rate = self.generateAudioMultiSpeaker(test_text, test_voices, test_lang)
        test_audio_file = self.generateAudioFile(test_audio, sample_rate)

        expected_result = (
            "Speaker A: This is a fascinating meeting that we are having today.\n" + 
            "Speaker B: I have never in my life attended a more interesting meeting.\n" 
        )
        self.assertEqual(expected_result, transcribe_with_speakers(test_audio_file))
