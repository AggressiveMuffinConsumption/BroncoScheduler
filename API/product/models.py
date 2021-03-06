from re import T
from django.db import models
from io import BytesIO
from PIL import Image

from django.core.files import File
from django.db import models
from django.forms import EmailField

class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField()

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/{self.slug}/'

class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products',on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    slug = models.SlugField()
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='uploads/',blank=True,null=True)
    thumbnail = models.ImageField(upload_to='uploads/',blank=True,null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-date_added',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/{self.category.slug}/{self.slug}/'

    def get_image(self):
        if self.image:
            return 'http://127.0.0.1:8000' + self.image.url
        return ''

    def get_thumbnail(self):
        if self.thumbnail:
            return 'http://127.0.0.1:8000' + self.thumbnail.url
        else:
            if self.image:
                self.thumbnail = self.make_thumbnail(self.image)
                self.save()

                return 'http://127.0.0.1:8000' + self.thumbnail.url
            else:
                return ''       

    def make_thumbnail(self,image,size=(300,200)):  
        img  = Image.open(image)    
        img.convert('RGB')
        img.thumbnail(size)
        
        thumb_io = BytesIO()
        img.save(thumb_io, 'JPEG', quality = 85)

        thumbnail = File(thumb_io, name=image.name)

        return thumbnail

class Department(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField()

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/{self.slug}/'

class Program(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField()

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/{self.slug}/'

class Classes(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField()
    prereq = models.ManyToManyField('self', blank = True)
    coreq = models.ForeignKey('self', null = True, related_name= "coreqclass", on_delete=models.SET_NULL, blank = True)
    standing = models.IntegerField()
    department = models.ForeignKey(Department, null = True, related_name='classes',on_delete=models.SET_NULL)
    units = models.IntegerField(default=3)
    program = models.ManyToManyField(Program)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/{self.department.slug}/{self.slug}/'

class Student(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    slug = models.SlugField()
    standing = models.IntegerField(default=1)
    degree = models.ForeignKey(Program, null = True, related_name='degree',on_delete=models.SET_NULL,default = 1)    
    email = models.EmailField(default = "blank@cpp.edu")

    class Meta:
        ordering = ('lastname',)

    def __str__(self):
        return self.firstname + " " +self.lastname

    def get_absolute_url(self):
        return f'/{self.username}/'
