from django.db import models

class AudioFile(models.Model):
    title = models.CharField(max_length=255)
    audio_file = models.FileField(upload_to='audio_files/')
    audio_url = models.URLField(blank=True)  # New field for storing the audio URL
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        app_label = 'assemblyaimodule'

    def __str__(self):
        return self.title
