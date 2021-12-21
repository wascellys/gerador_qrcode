from django.conf.urls.static import static
from django.urls import path

from cardapiovirtual import settings
from restcon.views import gerador_qrcode, gerador_qrcode_pdf, url_cardapio

urlpatterns = [
    # path('', home, name='home'),
    # path('produtos/<int:pk>', produtos, name='produtos'),
    path('gerador_qrcode', gerador_qrcode, name='gerador_qrcode'),
    path('gerador_qrcode_pdf', gerador_qrcode_pdf, name='gerador_qrcode_pdf'),
    path('url_cardapio', url_cardapio, name='url_cardapio'),
]