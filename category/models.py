from django.db import models
from authentication.models import User, UserProfile
from re import I
from django.db import models
from django.utils import timezone
from django.dispatch import receiver
from more_itertools import quantify
from django.db.models import Sum


class Category(models.Model):
    name = models.CharField(max_length=250, unique=True)
    description = models.TextField()
    status = models.CharField(
        max_length=2, choices=(("1", "Active"), ("2", "Inactive")), default=1
    )
    date_created = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name







# class Invoice(models.Model):
#     transaction = models.CharField(max_length=250)
#     customer = models.CharField(max_length=250)
#     total = models.FloatField(default=0)
#     date_created = models.DateTimeField(default=timezone.now)
#     date_updated = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return self.transaction

#     def item_count(self):
#         return Invoice_Item.objects.filter(invoice=self).aggregate(Sum("quantity"))[
#             "quantity__sum"
#         ]


# class Invoice_Item(models.Model):
#     invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     stock = models.ForeignKey(Stock, on_delete=models.CASCADE, blank=True, null=True)
#     price = models.FloatField(default=0)
#     quantity = models.FloatField(default=0)

#     def __str__(self):
#         return self.invoice.transaction


# @receiver(models.signals.post_save, sender=Invoice_Item)
# def stock_update(sender, instance, **kwargs):
#     stock = Stock(product=instance.product, quantity=instance.quantity, type=2)
#     stock.save()
#     # stockID = Stock.objects.last().id
#     Invoice_Item.objects.filter(id=instance.id).update(stock=stock)


# @receiver(models.signals.post_delete, sender=Invoice_Item)
# def delete_stock(sender, instance, **kwargs):
#     try:
#         stock = Stock.objects.get(id=instance.stock.id).delete()
#     except:
#         return instance.stock.id
