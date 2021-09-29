from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('store.urls', namespace='store')),
    path('carrinho/', include('carrinho.urls', namespace='carrinho')),
    path('conta/', include('conta.urls', namespace='conta')),
    path('pedidos/', include('pedidos.urls', namespace='pedidos')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
