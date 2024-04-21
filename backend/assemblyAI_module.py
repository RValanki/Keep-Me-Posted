""" This is the module that stores all functions related to Assembly AI"""

import assemblyai as aai

aai.settings.api_key = "620d4459badf4480a039c646ab4c3216"

def  transcribe(audioURL) -> str:
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

