from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def generate_summary(request):

    ## Implement the summarisation logic here
    return HttpResponse("Generated summary goes here")