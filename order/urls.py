import imp
from os import name
from django.urls import path, include
from .views import Order

from order import views

urlpatterns = [
   
    path('checkout/',views.checkout),
]