from unicodedata import category
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
    sub_category = models.ForeignKey(
        SubCategory, on_delete=models.CASCADE, null=True, blank=True
    )

    def __str__(self) -> str:
        return f"{self.id}"
