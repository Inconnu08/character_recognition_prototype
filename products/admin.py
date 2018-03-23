from django.contrib import admin
from products.models import Products, AttributeType, ProductVariance, ProductVarianceAttribute

admin.site.register(Products)
admin.site.register(AttributeType)
admin.site.register(ProductVariance)
admin.site.register(ProductVarianceAttribute)
