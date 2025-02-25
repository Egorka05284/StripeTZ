from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
# import stripe
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, FormView

from items.models import Items

# Create your views here.


class ItemShowView(DetailView):
    model = Items
    template_name = 'items/itemshow.html'
    context_object_name = 'item'

    def get(self, request, item_id) -> HttpResponse:
        item = Items.objects.get(id=item_id)
        return render(self.request, 'items/itemshow.html', {'item': item})

class ItemsListView(ListView):
    model = Items
    template_name = 'items/index.html'
    paginate_by = 3
    context_object_name = 'items'

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)

class ItemBuingView(DetailView):
    model = Items
    template_name = 'items/itembuying.html'
    context_object_name = 'item'

    def get(self, request, item_id) -> HttpResponse:
        item = Items.objects.get(id=item_id)
        return render(self.request, 'items/itembuying.html', {'item': item})