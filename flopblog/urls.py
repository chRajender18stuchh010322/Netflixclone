from django.urls import path, include
from .import views


app_name='flopblog'

urlpatterns = [
    path('create', views.create, name='create'),
    path('flop/', views.Flopblog, name='flop'),


]
