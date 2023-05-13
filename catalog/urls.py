from django.urls import path, include
from rest_framework.routers import DefaultRouter
from catalog import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r"product", views.ProductViewset, basename="product_viewset")
router.register(r"category", views.CategoryViewset, basename="category_viewset")
router.register(
    r"subcategory", views.SubCategoryViewset, basename="subcategory_viewset"
)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path("", include(router.urls)),
]
