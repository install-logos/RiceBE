from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.QuerySearchView.as_view()),
]
