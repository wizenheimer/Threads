from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.decorators import action, api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from django_elasticsearch_dsl_drf.viewsets import DocumentViewSet
from catalog.documents import ProductDocument
from catalog.serializers import ProductDocumentSerializer
from .models import Product, Category, SubCategory
from .serializers import ProductSerializer, CategorySerializer, SubCategorySerializer
from .pagination import StandardResultsSetPagination, LargeResultsSetPagination
from django_elasticsearch_dsl_drf.constants import SUGGESTER_COMPLETION
from django_elasticsearch_dsl_drf.filter_backends import (
    SearchFilterBackend,
    FilteringFilterBackend,
    SuggesterFilterBackend,
)


class ProductDocumentViewset(DocumentViewSet):
    document = ProductDocument
    serializer_class = ProductDocumentSerializer
    pagination_class = StandardResultsSetPagination

    filter_backends = [
        SearchFilterBackend,
        FilteringFilterBackend,
        SuggesterFilterBackend,
    ]

    search_fields = (
        "brand",
        "title",
        "sub_category",
    )

    filter_fields = {"sub_category": "sub_category.title"}

    suggester_fields = {
        "title": {
            "field": "title.suggest",
            "suggesters": [
                SUGGESTER_COMPLETION,
            ],
        },
        "brand": {
            "field": "brand.suggest",
            "suggesters": [
                SUGGESTER_COMPLETION,
            ],
        },
    }


class ProductViewset(viewsets.ReadOnlyModelViewSet):
    queryset = Product.objects.filter(is_active=True)
    serializer_class = ProductSerializer
    pagination_class = StandardResultsSetPagination
    search_fields = [
        "brand",
        "sub_category",
    ]


class CategoryViewset(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = LargeResultsSetPagination


class SubCategoryViewset(viewsets.ReadOnlyModelViewSet):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer
    pagination_class = LargeResultsSetPagination
