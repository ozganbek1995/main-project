from django.contrib import admin
from .models import *
from django.contrib.admin import ModelAdmin

class ShopAdmin(ModelAdmin):
    list_display = ['name', 'description', 'ret_hos_fir']



admin.site.register(Viloyat)
admin.site.register(Tuman)
admin.site.register(Shop, ShopAdmin)
admin.site.register(Product)

admin.site.register(Currency)
admin.site.register(Types)



