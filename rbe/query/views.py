import json

from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse, JsonResponse
from django.db.models import Q

from .models import Package
from .utils import prep_search_results


def index(request):
    return HttpResponse("Welcome to the RiceDB back end server. To query for rices, please use [url]/?q=[search term]")


class QuerySearchView(View):
	"""
	View for handling package searches
	"""
	def get(self, request):
		search_string = request.GET.get('q', 'Nothing')
		query_obj = Package.objects.filter(Q(name__icontains = search_string) | 
			Q(description__icontains = search_string))
		if query_obj:
			response = prep_search_results(query_obj)
			return JsonResponse(response, safe=False)
		return HttpResponse("No Result Found for %s" % search_string)
