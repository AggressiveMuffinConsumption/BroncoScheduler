from django.http import Http404, JsonResponse
from django.shortcuts import render
from rest_framework.parsers import JSONParser 
from rest_framework import status
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response

from.models import Product, Classes , Department, Student
from .serializers import ProductSerializer ,ClassSerializer, StudentSerializer

class LatestProductsList(APIView):
    def get(self, request, format=None):
        products = Product.objects.all()[0:4]
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

class ClassesList(APIView):
    def get(self, request, format=None):
        classes = Classes.objects.all()
        serializer = ClassSerializer(classes, many=True)
        return Response(serializer.data)

class StudentList(APIView):
    permission_classes = (permissions.AllowAny,)
    def get(self, request, format=None):
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        student_data = JSONParser().parse(request)
        student_serializer = StudentSerializer(data=student_data)
        if student_serializer.is_valid():
            student_serializer.save()
            return JsonResponse(student_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(student_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


class ProductDetail(APIView):
    def get_object(self,category_slug, product_slug):
        try:
            return Product.objects.filter(category__slug=category_slug).get(slug=product_slug)
        except Product.DoesNotExist:
            raise Http404
    
    def get(self, request, category_slug, product_slug, format=None):
        product = self.get_object(category_slug, product_slug)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

class ClassesDetail(APIView):
    def get_object(self,classes_slug,department_slug):
        try:
            return Classes.objects.filter(department__slug=department_slug).get(slug=classes_slug)
        except Product.DoesNotExist:
            raise Http404
    
    def get(self, request, classes_slug, department_slug, format=None):
        product = self.get_object(classes_slug, department_slug)
        serializer = ClassSerializer(product)
        return Response(serializer.data)
    
class StudentDetail(APIView):
    def get_object(self,student_slug):
        try:
            return Classes.objects.get(slug=student_slug)
        except Product.DoesNotExist:
            raise Http404
    
    def get(self, request, student_slug, format=None):
        product = self.get_object(student_slug)
        serializer = StudentSerializer(product)
        return Response(serializer.data)