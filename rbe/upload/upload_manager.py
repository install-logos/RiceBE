"""Handle Uploads from client"""
import os, urllib2, json, zipfile, shutil, subprocess
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
		temp = PACKAGE_DIR + "temp"
		subprocess.call(["git","clone",self.upstream_url,temp])
		os.chdir(temp)
		
		if INFO_FILE not in os.listdir('.'):
			os.chdir('..')
			upload_response['error'] = 'Missing package metadata'
			shutil.rmtree('temp')
			os.mkdir('temp')
			os.chdir('..')
			return upload_response
		# if checkSpam():
		#	upload_response['error'] = 'Package is SPAM'
		#	return upload_response

		# if checkPlagiarism():
		#	upload_response['error'] = 'Package is Plagiarism'
		#	return upload_response

		# create and save the package
		with open(INFO_FILE) as f:
			upload_data = json.loads("".join(f.readlines()))
		# this could fail if they pass some bad data
		# TODO: figure out how we want this to behave in that case
		uploaded_package = Package(**upload_data)
		uploaded_package.save()
		upload_response['success'] = "Package uploaded successfully!"
		
		# Clean up files
		os.chdir('..')
		shutil.rmtree('temp')
		os.mkdir('temp')
		os.chdir('..')

		return upload_response
