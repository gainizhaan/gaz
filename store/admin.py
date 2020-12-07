from django.contrib import admin

# Register your models here.
# here we register out models so they are visible on the screen

from .models import *  #the * symbol allows importing modules without referring them in the code later

admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)