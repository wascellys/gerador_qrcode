from django.conf.urls.static import static
from django.urls import path

from cardapiovirtual import settings
from restcon.views import gerador_qrcode, gerador_qrcode_pdf, url_cardapio

urlpatterns = [
    path('gerador_qrcode', gerador_qrcode, name='gerador_qrcode'),
]


