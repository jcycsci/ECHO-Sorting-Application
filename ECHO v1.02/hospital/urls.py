from django.conf.urls import url
from . import views

app_name = 'hospital'

urlpatterns = [
	# /hospital/
	url(r'^$', views.IndexView.as_view(), name='index'),

	# /hospital/71/
	url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),

]