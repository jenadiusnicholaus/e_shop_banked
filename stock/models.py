from django.db import models
from django.utils import timezone
from products.models import Product


class Stock(models.Model):
    name = models.CharField(max_length=13, null=True, unique=True)
    status = models.CharField(
        max_length=2, choices=(("1", "Stock-in"), ("2", "Stock-Out")), default=1
    )
    date_created = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class StockItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    stock = models.ForeignKey(Stock, on_delete=models.SET_NULL, null=True)
    description = models.TextField(null=True)
    qty = models.FloatField(default=0)

    # Single product price
    unit_price = models.CharField(max_length=12)

    # Single product selling price
    unit_selling_price = models.CharField(max_length=12)

    # Single product Estimated  profit
    unit_estmated_profit = models.CharField(max_length=12, null=True, blank=True)

    # total Estimated  profit
    total_estmated_profit = models.CharField(max_length=12, null=True, blank=True)

    # total selling price
    total_selling_price = models.CharField(max_length=12, null=True, blank=True)

    status = models.CharField(
        max_length=2, choices=(("1", "in-stock"), ("2", "out-stock")), default=1
    )

    date_created = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product.code + " - " + self.product.name

    def save(self, *args, **kwargs):
        self.get_unit_es_profit()
        self.total_selling_price = self.get_total_selling_price()
        self.total_estmated_profit = self.get_total_est_profit()
        super(StockItem, self).save(*args, **kwargs)

    def get_total_selling_price(self):
        total = 0.0
        if self.unit_selling_price:
            total = self.qty * float(self.unit_selling_price)

            return total
        return total

    def get_total_est_profit(self):
        total = 0.0
        if self.unit_estmated_profit:
            total = self.qty * float(self.unit_estmated_profit)

            return total
        return total

    def get_unit_es_profit(self):
        self.unit_estmated_profit = float(self.unit_selling_price) - float(
            self.unit_price
        )
