from django.views import generic
from .models import Item

class IndexView(generic.ListView):
	template_name = 'hospital/index.html'
	context_object_name = 'all_items'

	def get_queryset(self):
		return Item.objects.all()


class DetailView(generic.DetailView):
	model = Item
	template_name = 'hospital/detail.html'


	
	
		