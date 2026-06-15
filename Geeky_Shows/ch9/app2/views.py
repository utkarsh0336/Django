from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def myapp2(request):
    return HttpResponse(f"<h1> Hello My App 2 </h1>")

