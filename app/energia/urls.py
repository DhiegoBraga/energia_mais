from django.urls import path, include
from . import views

app_name = 'energia'

urlpatterns = [
    path('', views.index, name='index'),
]