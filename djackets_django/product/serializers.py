from rest_framework import serializers

from.models import Category, Product, Classes, Student

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
            "slug",

        )

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = (
            "id",
            "firstname",
            "lastname",
            "username",
            "get_absolute_url",
            "standing",
            "degree",
            "email",

        )