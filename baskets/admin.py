from django.contrib import admin

from baskets.models import Basket


# Register your models here.
class BasketAdmin(admin.TabularInline):
    model = Basket
    fields = ('product', 'quantity', 'created_timestamp', 'updated_timestamp',)
    readonly_fields = ('created_timestamp', 'updated_timestamp')
    extra = 0
