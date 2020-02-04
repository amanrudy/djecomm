from django import template
from core.models import Order, OrderItem


register = template.Library()

# @register.filter
# def cart_item_count(user):
# 	if user.is_authenticated:
# 		qs = Order.objects.filter(user=user,ordered=False)		
# 		if qs.exists():
# 			try:
# 				quantity = qs[0].items.all().first().quantity
# 			except:
# 			    quantity = 0
# 			return quantity
# 	return 0

@register.filter
def cart_item_count(user):
	if user.is_authenticated:
		qs = Order.objects.filter(user=user,ordered=False)		
		if qs.exists():
			return qs[0].items.count()
	return 0
