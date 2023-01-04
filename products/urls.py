from django.urls import path

from .views import ProductImageView, ProductView


urlpatterns = [
    path("", ProductView.as_view(), name="products"),
    path("images", ProductImageView.as_view(), name="images"),
]