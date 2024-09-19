# viewer/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Root URL for the app
]
