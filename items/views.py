import stripe
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView, FormView, TemplateView
from TestTask import settings
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

    
def buyitem(request, item_id):
    item = Items.objects.get(id=item_id)
    item_price = str(item.price)
    item_price = item_price.replace('.', '')
    item_price = int(item_price)
    stripe.api_key = settings.STRIPE_SECRET_KEY
    intent = stripe.PaymentIntent.create(
        amount=item_price,
        currency='usd',
        metadata= {'userid': request.user.id}
    )
    return render(request, 'items/itembuying.html', {'item': item, 'client_secret': intent.client_secret, 
                                                        'STRIPE_PUBLISHABLE_KEY': settings.STRIPE_PUBLISHABLE_KEY})