from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Welcome to the RiceDB back end server. To query for rices, please use [url]/?q=[search term]")

class QuerySearchView(View):
	def get(self, request):
		pack = request.GET.get('q', 'Nothing')
		return HttpResponse("You sent a query for " + pack + ". Please wait a bit")
