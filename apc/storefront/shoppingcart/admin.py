from django.contrib import admin
from .authentication.models import MenuItem, Customer, DeliveryAgent, Staff, Order, OrderDetail, Ingredint, Recipe, Supplier, Category

# Register your models here.

admin.site.register(MenuItem)
admin.site.register(Customer)
admin.site.register(Category)
admin.site.register(DeliveryAgent)
admin.site.register(Staff)
admin.site.register(Order)
admin.site.register(OrderDetail)
admin.site.register(Ingredint)
admin.site.register(Recipe)
admin.site.register(Supplier)