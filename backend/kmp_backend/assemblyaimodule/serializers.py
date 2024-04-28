from rest_framework import serializers

class AudioTranscriptionSerializer(serializers.Serializer):
    audio_url = serializers.CharField()  # Assuming a maximum URL length of 255 characters
