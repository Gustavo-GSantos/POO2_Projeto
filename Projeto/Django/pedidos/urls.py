from django.urls import path
from django.views.generic import TemplateView

from . import views

app_name = 'pedidos'

urlpatterns = [path('add/', views.add, name='add'),
               path('pedidoconfirmado/', views.confirmar_pedido, name='pedidoconfirmado')]