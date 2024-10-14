from django.urls import path
from inicio.views import inicio,compradores

urlpatterns=[
    path('', inicio),
    path('compradores/', compradores) 
]