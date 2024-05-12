from django.urls import path
from . import views

urlpatterns = [
    path('summariser/', views.generate_summary, name='summariser'),
]
