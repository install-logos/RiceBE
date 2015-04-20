"""Handle Uploads from client"""
import os, urllib2, json, zipfile, shutil
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
		uopener = urllib2.urlopen(self.upstream_url)
		data = uopener.read()
		with open(temp,"wb") as fout:
			fout.write(data)
		if not (os.path.exists(temp) and zipfile.is_zipfile(temp)):
			upload_response['error'] = "BAD URL or Zipfile"
			return upload_response

		z = zipfile.ZipFile(temp)

 		for name in z.namelist():
			z.extract(name, PACKAGE_DIR + "temp/")

		os.chdir(PACKAGE_DIR + "temp")
		path_files = os.listdir('.')
 		if len(path_files) == 1 and os.path.isdir(path_files[0]):
            		os.chdir(path_files[0])
            		for f in os.listdir('.'):
                		os.rename('./'+f,'../'+f)
        		os.chdir('../')
       			os.rmdir(path_files[0])
	
		
		
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
