from django.urls import path
from .views import (
	HomeView,
	ItemDetailView,
	checkout,
	add_to_cart,
	remove_from_cart,
	OrderSummaryView,
	remove_sigle_item_from_cart,
	add_single_item_to_cart
)

app_name = 'core'

urlpatterns = [
	path('', HomeView.as_view(), name='home'),
	path('checkout/', checkout, name='checkout'),
	path('order-summary/', OrderSummaryView.as_view(), name='order-summary'),
	path('product/<slug>/', ItemDetailView.as_view(), name='product'),
	path('add-to-cart/<slug>/', add_to_cart, name='add-to-cart'),
	path('remove-from-cart/<slug>/', remove_from_cart, name='remove-from-cart'),
	path('remove-item-from-cart/<slug>/', remove_sigle_item_from_cart, name='remove-sigle-item-from-cart'),
	path('add-item-to-cart/<slug>/', add_single_item_to_cart, name='add-single-item-to-cart'),
	]
	