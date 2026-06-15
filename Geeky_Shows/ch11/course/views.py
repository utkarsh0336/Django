from django.shortcuts import render

# Create your views here.

def learn_django(req):
    coursename = {'cname': 'JS'}

    return render(req,'course/django.html',context=coursename)

def learn_fastapi(req):
    return render(req,'course/fastapi.html',{'rest': "REST API"})