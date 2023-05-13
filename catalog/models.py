from .utility import check_link_rot
from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self) -> str:
        return f"{self.id}"


class SubCategory(models.Model):
    title = models.CharField(max_length=255)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, null=True, blank=True
    )

    def __str__(self):
        return f"{self.id}"


class Product(models.Model):
    brand = models.CharField(max_length=255)
    product_type = models.CharField(max_length=255)
    alt_type = models.CharField(max_length=255)
    product_url = models.URLField()
    title = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    sub_category = models.ForeignKey(
        SubCategory, on_delete=models.CASCADE, null=True, blank=True
    )

    def save(self, *args, **kwargs):
        if check_link_rot(self.product_url):
            self.is_active = False
        return super(Product, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return f"{self.id}"
