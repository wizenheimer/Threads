from rest_framework import serializers
from .models import Category, SubCategory, Product
from django_elasticsearch_dsl_drf.serializers import DocumentSerializer

from catalog.documents import ProductDocument


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class SubCategorySerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)

    class Meta:
        model = SubCategory
        fields = "__all__"
        extra_fields = ["category"]

    def get_field_names(self, declared_fields, info):
        expanded_fields = super(SubCategorySerializer, self).get_field_names(
            declared_fields, info
        )

        if getattr(self.Meta, "extra_fields", None):
            return expanded_fields + self.Meta.extra_fields
        else:
            return expanded_fields


class ProductSerializer(serializers.ModelSerializer):
    subcategory = SubCategorySerializer(read_only=True)

    class Meta:
        model = Product
        fields = "__all__"
        extra_fields = ["subcategory"]

    def get_field_names(self, declared_fields, info):
        expanded_fields = super(ProductSerializer, self).get_field_names(
            declared_fields, info
        )

        if getattr(self.Meta, "extra_fields", None):
            return expanded_fields + self.Meta.extra_fields
        else:
            return expanded_fields


class ProductDocumentSerializer(DocumentSerializer):
    class Meta:
        document = ProductDocument

        fields = (
            "brand",
            "title",
            "sub_category",
        )
