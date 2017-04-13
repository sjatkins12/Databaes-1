from django.contrib import admin

from .models import *

# Register your models here.
admin.site.register(Item)
admin.site.register(Order)
admin.site.register(Supplier)
admin.site.register(SellingOrder)
admin.site.register(SellingCycle)
admin.site.register(InterestGroup)
admin.site.register(SubCategory)
admin.site.register(Category)
admin.site.register(Box)
admin.site.register(Vote)
