from django.contrib import admin

from listings.models import Merchant, Product

class MerchantAdmin(admin.ModelAdmin):
    list_display=('name', 'category', 'type')
    


# Register your models here.
models=[Merchant, Product]

admin.site.register(models)
