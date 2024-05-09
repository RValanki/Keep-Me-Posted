# Start by making sure the `assemblyai` package is installed.
# If not, you can install it by running the following command:
# pip install -U assemblyai
#
# Note: Some macOS users may need to use `pip3` instead of `pip`.

from assemblyAI_module import *

# URL of the file to transcribe
FILE_URL = "https://github.com/AssemblyAI-Examples/audio-examples/raw/main/20230607_me_canadian_wildfires.mp3"


# create a file to write the transcription to
file_handler = open("transcript.txt", "w")
file_handler.write(transcribe_with_speakers(FILE_URL))
file_handler.close()