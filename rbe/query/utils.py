"""Utilities for the Query Search View"""
from django.forms.models import model_to_dict


def prep_search_results(results):
	"""
		Converts the models passed in the query object to 
		seralizable dicts
	"""
	prepared_results = []
	for rice in results:
		prepared_results.append(model_to_dict(rice))
	return prepared_results
