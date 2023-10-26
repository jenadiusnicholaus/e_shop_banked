from django.db import models
from django.utils import timezone
from category.models import Category
import random
import string


class Product(models.Model):
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
    )
    code = models.CharField(max_length=100, blank=True, unique=True, null=True)
    name = models.CharField(max_length=250, blank=True, unique=True, null=True)
    description = models.TextField()
    price = models.FloatField(default=0)
    status = models.CharField(
        max_length=2, choices=(("1", "Active"), ("2", "Inactive")), default=1
    )
    date_created = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.code) + " - " + str(self.name)

    def save(self, *args, **kwargs):
        if not self.code:
            self.code = self.generate_value()

        super(Product, self).save(*args, **kwargs)

    def generate_value(self):
        return f" {self.name}-{''.join(random.choice(string.ascii_letters) for _ in range(10))}"
