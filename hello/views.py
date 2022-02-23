import requests

from django.shortcuts import render
from django.http import HttpResponse
from .models import Greeting

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
    #return render(request, 'ricky.html')

def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})
