import requests
import numpy
from django.shortcuts import render
from django.http import HttpResponse
from .models import Greeting
from scipy import special
import pandas
import scrapy
import unittest

# Create your views here.
def index(request):
    r = requests.get('https://httpbin.org/status/418')
    print(r.text)
    return HttpResponse('<pre>' + r.text + '</pre>')

def say_hello(request):
    return render(request, 'hello.html')

def johnathan(request):
    return render(request, 'johnathan.html')

def ricky(request):
    pVal = special.perm(7, 3, exact = True)
    eVal = special.exp2(4)
    context = {
        "permVal" : pVal,
        "exp2Val" : eVal
    }
    return render(request, 'ricky.html', context)

def april(request):
    return render(request, 'april.html')

def danica(request):
    return render(request, 'danica.html')

def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})

def matrix(request):
    aString, bString ,cString ,c1String = matrixUse()
    context = {
        "matrix_a": aString,
        "matrix_b": bString,
        "matrix_c": cString,
        "matrix_c1": c1String
    }
    template_name="numpy.html"
    return render(request, template_name, context)

def matrixUse():
    a = numpy.array([[1,2,3],[4,5,6],[7,8,9]])
    b = numpy.array([2,2,2])
    c = a * b #element wise multiplication
    print(c)
    print("")
    c1 = b @ a #matrix multiplication
    print(c1)
    aString = numpy.array2string(a)
    bString = numpy.array2string(b)
    cString = numpy.array2string(c)
    c1String = numpy.array2string(c1)
    return aString,bString,cString,c1String

def pandas(request) :
    names = ["Peter", "Paul", "Tracy", "Trucy"]
    years = [3, 2, 4, 1]
    majors = ["Computer Science", "Computer Information System", "Computer Engineering", "Undeclared"]
    test2 = pandas.DataFrame({
        "Name" : names,
        "Year" : years,
        "Major" : majors
    })
    context = {test2}
    template_name = "pandas.html"
    return render(request, template_name, context)

class MySpider(scrapy.Spider):
    name = 'testspider'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['https:quotes.toscrape.com/']

    def parse(self, response):
        quotes = response.xpath("//div[@class='quote']").extract()
        yield{'quotes': quotes}

def scrapy(request):
    contexts = {quotes}
    template_name = "scrapy.html"
    return render(request, template_name, contexts)
