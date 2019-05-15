from django.urls import path
from .views import *

urlpatterns = [
    path('home/', ListMeme),
    path('add/', NewMeme),
]
