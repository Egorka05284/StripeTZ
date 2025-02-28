from django.urls import path

from items import views

app_name = 'items'

urlpatterns = [
    path('items/', views.ItemsListView.as_view(), name='items'),
    path('item/<int:item_id>/', views.ItemShowView.as_view(), name='item'),
    path('buy/<int:item_id>/', views.buyitem, name='buying'),
]
