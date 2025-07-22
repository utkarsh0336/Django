from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Product
from math import ceil
from django.views.decorators.csrf import csrf_exempt
import requests
import json

# Create your views here.
def index(request):
    # products = Product.objects.all()
    # print(products)
    # n = len(products)
    # nSlides = n // 4 - ceil((n / 4) - (n // 4))

    allProds = []
    catprods = Product.objects.values('category' , 'id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(category = cat)
        n = len(prod)
        nSlides = n // 4 - ceil((n / 4) - (n // 4))
        allProds.append([prod , range(1,nSlides) , nSlides])

    # params = {'no_of_slides' : nSlides , 'range' : range(1,nSlides), 'product' : products}
    # allProds = [[products , range(1 , nSlides) , nSlides] ,
    #             [products , range(1 , nSlides) , nSlides]]
    params = {'allProds' : allProds}
    return render(request , 'shop/index.html' , params)

def about(request):
    return render(request , 'shop/about.html')

def contact(request):
    return HttpResponse("We are at contact")

def tracker(request):
    return HttpResponse("We are at tracker")

def search(request):
    return HttpResponse("We are at search")

def productView(request):
    return HttpResponse("We are at productView")

def checkout(request):
    return HttpResponse("We are at checkout")

@csrf_exempt
def ollama_chat(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            user_message = data.get("message", "")
            
            if not user_message.strip():
                return JsonResponse({"error": "Message cannot be empty"}, status=400)
            
            ollama_url = "http://localhost:11434/api/chat"
            payload = {
                "model": "llama2",  # You can change this to any model you have installed
                "messages": [{"role": "user", "content": user_message}],
                "stream": False
            }
            
            # Increased timeout to 60 seconds for first response and 30 seconds for subsequent
            # First request might take longer due to model loading
            timeout = 60 if "first_request" not in request.session else 30
            request.session["first_request"] = True
            
            response = requests.post(ollama_url, json=payload, timeout=timeout)
            
            if response.status_code == 200:
                ollama_response = response.json()
                reply = ollama_response.get("message", {}).get("content", "Sorry, I couldn't generate a response.")
                return JsonResponse({"reply": reply})
            else:
                return JsonResponse({
                    "error": f"Ollama server returned status {response.status_code}. Make sure Ollama is running."
                }, status=500)
                
        except requests.exceptions.ConnectionError:
            return JsonResponse({
                "error": "Cannot connect to Ollama server. Please make sure Ollama is running on localhost:11434"
            }, status=503)
        except requests.exceptions.Timeout:
            return JsonResponse({
                "error": f"Request to Ollama timed out after {timeout} seconds. The model might be loading or the request is too complex. Please try again."
            }, status=408)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON in request"}, status=400)
        except Exception as e:
            return JsonResponse({
                "error": f"An unexpected error occurred: {str(e)}"
            }, status=500)
    
    return JsonResponse({"error": "Only POST requests are allowed"}, status=405)






