from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse, JsonResponse
from django.db.models import Q

# Need to import models from Query
# from .models import Package
import os, urllib.request, json, zipfile


class UploadView(View):
	"""
	View for handling user uploads
	"""
	def post(self, request):
		upstream  = request.POST.get('upstream','Nothing')
		path = os.getcwd() + "/packages/"
		temp = path + "temp.zip"
		urllib.request.urlretrieve(upstream, temp)
		if not (os.path.exists(temp) or not zipfile.is_zipfile(temp_file):
			return(HttpResponse("Please verify the URL you gave is correct, it may be the URL for cloning
			, not downloading the repository"))
		z = zipfile.ZipFile(temp)
		for name in z.namelist():
			z.extract(name, path + "temp/")	
		# To be implemented
		if checkSpam():
			return(HttpResponse("This upload has been flagged as spam. 
			Your IP will be restricted from uploading for the next X minutes.
			Please verify the link you provided is correct and contact a site moderator
			if you have any further questions")
		# To be implemented
		if checkPlagiarism():
			return(HttpResponse("This upload has been flagged as a duplicate. If you believe this
			is an incorrect assumption, please contact a site moderator")
		# Insert the package into the database now	
		return(HttpResponse("Thanks for the upload"))

	def get(self, request):
		return(HttpResponse("Please try sending a POST request to this URL, it will not respond to GET requests"))
