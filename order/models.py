from django.conf import settings
from django.db import models
from django.utils import timezone
from django_countries.fields import CountryField
from social_core.utils import slugify
import uuid

from products.models import ProductModel


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, blank=True, null=True)
    complete_order = models.BooleanField(default=False, null=False, blank=False)
    transaction_id = models.CharField(max_length=255, null=True, blank=True)
    slug = models.SlugField(max_length=255, blank=True, null=True)
    date_order = models.DateTimeField(timezone.now(), blank=True, null=True)

    def __str__(self):
        return self.user.email

    def save(self, *args, **kwargs):
        self.transaction_id = uuid.uuid1()
        self.slug = slugify(f'{self.transaction_id}-{self.date_order}')
        super().save(*args, **kwargs)

    @property
    def get_cart_total(self):
        order_items = self.order_item.all()
        total = sum([item.get_total for item in order_items])
        return total

    @property
    def get_cart_items(self):
        order_items = self.order_item.all()
        total = sum([item.quantity for item in order_items])
        return total


class OrderItem(models.Model):
    product = models.ForeignKey(ProductModel, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, related_name='order_item', on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=1, null=True, blank=True)
    date_added = models.DateTimeField(timezone.now(), blank=True, null=True)

    class Meta:
        ordering = ('-date_added',)

    def __str__(self):
        return self.product.title

    @property
    def get_total(self):
        if self.product.discount_price > 0:
            price_discount = self.product.price - self.product.discount_price
            return price_discount * self.quantity
        return self.quantity * self.product.price


class ShippingAddress(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, blank=True)
    country = CountryField()
    city = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    state = models.CharField(max_length=255, blank=True, null=True)
    zip_code = models.IntegerField()
    date_added = models.DateTimeField(timezone.now())

    def __str__(self):
        return f'{self.city} {self.address}'
