from django.contrib import admin
from .models import Stock, StockData

class StockAdmin(admin.ModelAdmin):
    search_fields = ('id', 'name', 'symbol')

admin.site.register(Stock, StockAdmin)
admin.site.register(StockData)
