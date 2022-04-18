from rest_framework import serializers

from.models import Category, Product, Classes

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

class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classes
        fields = (
            "id",
            "name",
            "get_absolute_url",
            "prereq",
            "coreq",
            "standing",
            "department",
            "units",

        )