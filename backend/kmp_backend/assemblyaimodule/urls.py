from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('api/transcribe', views.transcribe, name='transcribe'),
    path('api/transcribe/speakers', views.transcribe_with_speakers, name='transcribe_with_speakers'),
]

