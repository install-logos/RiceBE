import json

from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse, JsonResponse

from .upload_manager import UploadManager

# Need to import models from Query
# from .models import Package


class UploadView(View):
	"""
	View for handling user uploads
	"""
	def post(self, request):
		print("Creating upload maanger")
		# upstream_url  = json.loads(request.body).get('upstream')
		upstream_url  = request.POST.get('upstream',None)
		upload_manager = UploadManager(upstream_url)
		print("Retrieving file")
		upload_status = upload_manager.upload()
		return JsonResponse(upload_status)

	def get(self, request):
		return(HttpResponse("Please try sending a POST request to this URL, it will not respond to GET requests"))
