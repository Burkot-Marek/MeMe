from django.urls import path
from .views import *

urlpatterns = [
    path('home/', ListMeme, name='Home'),
    path('add/', NewMeme, name='NewMeme'),
    path('edit/<int:id>/', EditMeme, name='EditMeme'),
    path('delete/<int:id>', DeleteMeme, name='DeleteMeme')
]
