from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import AudioTranscriptionSerializer
from . import assemblyAI_module as TS

@api_view(['POST'])
def transcribe(request):
    serializer = AudioTranscriptionSerializer(data=request.data)
    if serializer.is_valid():
        audio_file = request.data["audio_url"]
        transcription = TS.transcribe(audio_file)
        return Response({'transcription': transcription}, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def transcribe_with_speakers(request):
    serializer = AudioTranscriptionSerializer(data=request.data)
    if serializer.is_valid():
        audio_file = request.data["audio_url"]
        transcription = TS.transcribe_with_speakers(audio_file)
        return Response({'transcription': transcription}, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
