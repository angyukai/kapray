from django.shortcuts import render, render_to_response, RequestContext
from django.template import loader

# Create your views here.

def home(request):
    
    return render(request, 'signups/signups.html')