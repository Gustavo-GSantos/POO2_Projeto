from django.urls import path

from . import views

app_name = 'store'

urlpatterns = [
    path('', views.todosOsProdutos, name='todosOsProdutos'),
    path('item/<slug:slug>/', views.detalhe_produto, name='detalhe_produto'),
    path('search/<slug:slug_categorias>/', views.lista_categorias, name='lista_categorias')
]
