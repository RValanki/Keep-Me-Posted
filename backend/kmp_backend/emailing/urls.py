from django.urls import path
from . import views

urlpatterns = [
    path('emailer/', views.send_email, name='send email'),
]