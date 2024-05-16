from django.urls import path
from . import views

urlpatterns = [
    path('api/summariser', views.generate_summary, name='summariser'),
]
