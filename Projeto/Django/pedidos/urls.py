from django.urls import path
from . import views

app_name = 'pedidos'

urlpatterns = [path('add/', views.add, name='add'),]