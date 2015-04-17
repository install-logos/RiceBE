from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View
from django.http import HttpResponse, JsonResponse
from django.db.models import Q

# Need to import models from Query
# from .models import Package


class UploadView(View):
	"""
	View for handling user uploads
	"""
	@csrf_exempt
	def get(self, request):
		if request.method == 'POST':
			upstream = request.POST.get('upstream','Nothing')
		else:
			return HttpResponse('You did not send a proper POST request, please try again')
