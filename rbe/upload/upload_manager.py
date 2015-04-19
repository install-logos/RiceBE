"""Handle Uploads from client"""
import os, urllib.request, json, zipfile
from rice_verify import checkSpam, checkPlagarism
from query.models import Package

PACKAGE_DIR = os.getcwd() + "/packages/"
INFO_FILE = 'info.json'

class UploadManager(object):
	"""
	Manager to handle validating and uploading packages
	"""
	def __init__(self, upstream_url):
		self.upstream_url = upstream_url

	def upload(self):
		upload_response = {}
		temp = PACKAGE_DIR + "temp.zip"
		urllib.request.urlretrieve(upstream, temp)
		if not (os.path.exists(temp) or not zipfile.is_zipfile(temp_file)):
			upload_response['error'] = "BAD URL or Zipfile"
			return upload_response

		z = zipfile.ZipFile(temp)
		if INFO_FILE not in z.namelist():
			upload_response['error'] = 'Missing package metadata'
			return upload_response

 		for name in z.namelist():
			z.extract(name, PACKAGE_DIR + "temp/")

		if checkSpam():
			upload_response['error'] = 'Package is SPAM'
			return upload_response

		if checkPlagiarism():
			upload_response['error'] = 'Package is Plagiarism'
			return upload_response

		# create and save the package
		with open(INFO_FILE) as f:
			upload_data = json.loads("".join(f.readlines()))

		# this could fail if they pass some bad data
		# TODO: figure out how we want this to behave in that case
		uploaded_package = Package(**upload_data)
		uploaded_package.save()

		uploaded_package['success'] = "Package uploaded successfully!"

		return upload_response
