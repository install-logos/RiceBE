from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Welcome to the RiceDB back end server. To query for rices, please use [url]/query/?q=[search term]")
