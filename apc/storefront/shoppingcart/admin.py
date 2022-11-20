from django.contrib import admin
from .authentication.models import MenuItem, Customer, DeliveryAgent, Staff, Order, OrderDetails, Ingredints, Recipes, Supplier

# Register your models here.

admin.site.register(MenuItem)
admin.site.register(Customer)
admin.site.register(DeliveryAgent)
admin.site.register(Staff)
admin.site.register(Order)
admin.site.register(OrderDetails)
admin.site.register(Ingredints)
admin.site.register(Recipes)
admin.site.register(Supplier)