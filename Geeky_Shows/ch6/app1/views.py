from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def learn_django(request):
    return HttpResponse("Hello from Django")

def home(request):
    return HttpResponse("Hello from Home page")

def learn_python(request):
    return HttpResponse("<h1> Hello from Python </h1>")

def learn_math(request):
    a = 10 + 10
    return HttpResponse(a)