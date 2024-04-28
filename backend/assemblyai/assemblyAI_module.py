""" This is the module that stores all functions related to Assembly AI"""

import assemblyai as aai

aai.settings.api_key = "620d4459badf4480a039c646ab4c3216"

def transcribe(audioURL) -> str:
    '''This function takes an audio file and returns its transcript.
    
    Parameters:
        audioURL (str): The URL of the audio file you want to transcribe.
        
    Returns:
        str: Transcription text from the audio file.
    
    '''
    transcriber = aai.Transcriber()
    transcript = transcriber.transcribe(audioURL)

    if transcript.status == aai.TranscriptStatus.error:
        return transcript.error
    else:
        return transcript.text 

def transcribe_with_speakers(audioUrl) -> str:
    '''This function takes an audio file and returns its transcript with speakers.
    
    Parameters:
        audioURL (str): The URL of the audio file you want to transcribe.
        
    Returns:
        str: Transcription text with speakers from the audio file. Each line should have one speaker.
    
    '''
    transcriber = aai.Transcriber()
    config = aai.TranscriptionConfig(speaker_labels=True)
    transcript = transcriber.transcribe(audioUrl, config)

    if transcript.status == aai.TranscriptStatus.error:
        return transcript.error

    transcript_with_speakers = ""

    for utterance in transcript.utterances:
        transcript_with_speakers += f"Speaker {utterance.speaker}: {utterance.text}\n"

    return transcript_with_speakers

