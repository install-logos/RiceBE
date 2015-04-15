from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Welcome to the RiceDB back end server. To query for rices, please use [url]/?q=[search term]")

def query(request):
    pack = request.GET['q']
    return HttpResponse("You sent a query for " + pack + ". Please wait a bit")
