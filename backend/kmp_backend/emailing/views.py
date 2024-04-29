from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def send_email(request):
    
    # send with mailchimp here
    
    print("Send email function triggered")
    
    return HttpResponse("Some confirmation or error response")