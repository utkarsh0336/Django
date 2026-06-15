from django.urls import path,include
from course.views import learn_django,learn_fastapi

urlpatterns = [
    path("dj/",learn_django),
    path("fapi/",learn_fastapi)
]