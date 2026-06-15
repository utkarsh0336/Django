from django.urls import path
from app1.views import learn_django

urlpatterns = [
    path('dj/',learn_django,name="learn_django"),
    path('py/',learn_django,{"status": "OK"},name="learn_django"),
]