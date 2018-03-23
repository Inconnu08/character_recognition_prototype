from django.db import models
from django.db.models import Q
from django.utils import timezone

from products import choices


class AttributeType(models.Model):
    name = models.CharField(max_length=50, blank=False)
    value = models.CharField(max_length=100)

    def __str__(self):
        return "{}-{}".format(self.name, self.value)


class ProductQuerySet(models.query.QuerySet):
    def active(self):
        return self.filter(active=True)

    def featured(self):
        return self.filter(featured=True, active=True)

    def search(self, query):
        lookups = (Q(title__icontains=query) |
                  Q(description__icontains=query) |
                  Q(price__icontains=query)
                  )
        # tshirt, t-shirt, t shirt, red, green, blue,
        return self.active().filter(lookups).distinct()


class ProductManager(models.Manager):
    def get_queryset(self):
        return ProductQuerySet(self.model, using=self._db)

    def all(self):
        return self.get_queryset().active()

    def featured(self): #Product.objects.featured()
        return self.get_queryset().featured()

    def get_by_id(self, id):
        qs = self.get_queryset().filter(id=id) # Product.objects == self.get_queryset()
        if qs.count() == 1:
            return qs.first()
        return None

    def search(self, query):
        return self.get_queryset().search(query)


class Products(models.Model):
    title = models.CharField(max_length=225)
    brand = models.CharField(max_length=225, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    release_date = models.DateField(default=timezone.now)
    colors = models.CharField(max_length=225, choices=choices.COLORS, default='#000000', blank=True, null=True)
    qr_code = models.CharField(max_length=225, blank=True, null=True)
    barcode = models.CharField(max_length=225, blank=True, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=20, default=0.00)
    stock = models.IntegerField(default=1)
    active = models.BooleanField(default=True)
    featured = models.BooleanField(default=False)

    objects = ProductManager()

    def __str__(self):
        if self.qr_code:
            return self.qr_code + " : " + self.brand + " " + self.title
        else:
            return self.title


class ProductVariance(models.Model):
    product = models.ForeignKey(Products, related_name='variances', on_delete=models.CASCADE)
    type = models.ForeignKey(AttributeType, related_name='variances', null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return "{}:{}-{}".format(self.product.title, self.type.name, self.type.value)


class ProductVarianceAttribute(models.Model):
    product = models.ForeignKey(Products, related_name='product', on_delete=models.CASCADE)
    type = models.ForeignKey(AttributeType, related_name='attributes', null=True, blank=True, on_delete=models.CASCADE)
    weight = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    stock = models.IntegerField(default=0)
    size = models.CharField(max_length=4, blank=True, null=True)
    variance = models.ForeignKey(ProductVariance, related_name='attributes', on_delete=models.CASCADE)

    def __str__(self):
        return "{}:{}-{}".format(self.variance, self.type.name, self.type.value)