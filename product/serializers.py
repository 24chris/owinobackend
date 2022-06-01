from dataclasses import fields
from rest_framework import serializers

from .models import Category,Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            "id",
            "name",
            "get_absolute_url",
            "description",
            "price",
            "get_image",
            "get_thumbnail"
        )

class CategorySerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True)

    class Meta:
        model = Category
        fields = (
            "id",
            "name",
            "get_absolute_url",
            "get_slider_image",
            "get_slider_image2",
            "get_slider_image3",
            "get_slider_image4",
            "products",
            
        )