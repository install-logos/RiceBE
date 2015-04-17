from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse, JsonResponse
from django.db.models import Q

# Need to import models from Query
# from .models import Package


class UploadView(View):
	"""
	View for handling user uploads
	"""
	def post(self, request):
			return HttpResponse('You did not send a proper POST request, please try again')
