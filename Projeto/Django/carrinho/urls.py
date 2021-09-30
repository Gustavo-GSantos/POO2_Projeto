from django.urls import path

from . import views

app_name = 'carrinho'

urlpatterns = [
    path('', views.carrinho_resumo, name='carrinho_resumo'),
    path('add/', views.carrinho_add, name='carrinho_add'),
    path('delete/', views.carrinho_delete, name='carrinho_delete'),
    path('update/', views.carrinho_update, name='carrinho_update'),
    path('confirm/', views.pedido_confirmado, name='pedido_confirmado'),
]
