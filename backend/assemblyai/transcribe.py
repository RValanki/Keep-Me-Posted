# Start by making sure the `assemblyai` package is installed.
# If not, you can install it by running the following command:
# pip install -U assemblyai
#
# Note: Some macOS users may need to use `pip3` instead of `pip`.

import assemblyai as aai

aai.settings.api_key = "620d4459badf4480a039c646ab4c3216"
transcriber = aai.Transcriber()

config = aai.TranscriptionConfig(speaker_labels=True)
transcriber = aai.Transcriber(config=config)

# URL of the file o transcribe
FILE_URL = "https://github.com/AssemblyAI-Examples/audio-examples/raw/main/20230607_me_canadian_wildfires.mp3"

transcript = transcriber.transcribe(FILE_URL)
# You can also transcribe a local file by passing in a file path
# FILE_URL = './path/to/file.mp3'

# extract all utterances from the response
utterances = transcript.utterances

# create a file to write the transcription to
file_handler = open("transcript.txt", "w")

# For each utterance, print its speaker and what was said
for utterance in utterances:
  speaker = utterance.speaker
  text = utterance.text
  file_handler.write(f"Speaker {speaker}: {text}\n")

file_handler.close()