from django.urls import path
from . import views

urlpatterns = [
    path('api/sendemail', views.send_email, name='send_email'),
]