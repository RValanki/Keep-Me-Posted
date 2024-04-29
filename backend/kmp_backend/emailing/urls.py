from django.urls import path
from . import views

urlpatterns = [
    path('emailer/', views.add_subscriber, name='send email'),
]