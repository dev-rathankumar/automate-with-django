from django.db import models


class Stock(models.Model):
    name = models.CharField(max_length=255)
    symbol = models.CharField(max_length=50) # Unique stock symbol
    sector = models.CharField(max_length=100, null=True, blank=True)
    exchange = models.CharField(max_length=100)
    country = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name
    

class StockData(models.Model):
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE)
    current_price = models.CharField(max_length=25, null=True, blank=True)
    price_changed = models.CharField(max_length=25, null=True, blank=True)
    percentage_changed = models.CharField(max_length=25, null=True, blank=True)
    previous_close = models.CharField(max_length=25, null=True, blank=True)
    week_52_high = models.CharField(max_length=25, null=True, blank=True)
    week_52_low = models.CharField(max_length=25, null=True, blank=True)
    market_cap = models.CharField(max_length=25, null=True, blank=True)
    pe_ratio = models.CharField(max_length=25, null=True, blank=True)
    dividend_yield = models.CharField(max_length=25, null=True, blank=True)

    def __str__(self):
        return f"{self.stock} - {self.current_price}"