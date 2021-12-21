from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

# from restcon.api.viewsets import ProdutoViewSet, CategoriaViewSet, MesaViewSet, ContaViewSet, ProdutosContaViewSet, \
#     FuncionarioViewSet, FracionamentoViewSet,  ProdutoContaFracionamentoViewSet, PedacoViewSet

# router = routers.DefaultRouter()
# router.register('produtos', ProdutoViewSet, basename='produtos')
# router.register('categorias', CategoriaViewSet, basename='categorias')
# router.register('mesas', MesaViewSet, basename='mesas')
# router.register('conta', ContaViewSet, basename='conta')
# router.register('items-conta', ProdutosContaViewSet, basename='items-conta')
# router.register('funcionarios', FuncionarioViewSet, basename='funcionarios')
# router.register('fracionamentos', FracionamentoViewSet, basename='fracionamentos')
# router.register('tamanhos', PedacoViewSet, basename='tamanhos')
# router.register('conta-produto-fracionado', ProdutoContaFracionamentoViewSet, basename='conta-produto-fracionado')


urlpatterns = [
    # url('api/', include(router.urls)),
    path('admin/', admin.site.urls),
    path('cardapio/', include('restcon.urls')),


]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


# urlpatterns = [
#
#     url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
# ]
