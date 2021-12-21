from io import BytesIO, StringIO
import socket

import qrcode as qrcode
from PyPDF2 import PdfFileReader, PdfFileWriter
from django.http import HttpResponse
from django.shortcuts import render
from django.utils import autoreload
from pip._vendor.msgpack.fallback import xrange
from reportlab.lib.enums import TA_JUSTIFY

from reportlab.lib.pagesizes import landscape, A4, letter
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.utils import ImageReader
from reportlab.pdfgen import canvas
import qrcode

# from restcon.models import Categoria, Produto, Estabelecimento
import qrcode
from reportlab.platypus import Paragraph, Frame

from restcon.models import Cardapio


# def home(request):
#     empresa = Estabelecimento.objects.all().first()
#     categorias = Categoria.objects.filter(ativo=True).order_by('descricao')
#     return render(request,'home.html',{'categorias':categorias, 'empresa':empresa})
#
# def produtos(request, pk):
#     empresa = Estabelecimento.objects.all().first()
#     produtos = Produto.objects.filter(categoria__pk=pk, ativo=True).order_by('descricao')
#     return render(request, 'produtos.html', {'produtos': produtos, 'empresa':empresa})




def gerador_qrcode(request):


	if request.method == 'POST':
		import socket

		hostname = socket.gethostname()
		ip = socket.gethostbyname(hostname)
		qr = qrcode.QRCode(
				version=1,
				box_size=15,
				border=4
		)



		data = "https://praciano123.pythonanywhere.com/cardapio"
		qr.add_data(data)
		qr.make(fit=True)
		img = qr.make_image(fill='black', back_color='white')
		img.save('/home/praciano123/praciano123.pythonanywhere.com/static/img/qrcode_gerado.png')

		image = '/static/img/qrcode_gerado.png'

		return render(request, 'qrcode.html', {'qrcode': image})
	else:
		return render(request, 'qrcode.html')


def gerador_qrcode_pdf(request):
    import socket

    hostname = socket.gethostname()
    ip = socket.gethostbyname(hostname)
    qr = qrcode.QRCode(
        version=1,
        box_size=15,
        border=4
    )

    data = "https://praciano123.pythonanywhere.com/cardapio/cardapio.pdf"
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')
    img.save('/home/praciano123/praciano123.pythonanywhere.com/static/img/pdf.png')


    return render(request, 'qrcode.html', {'qrcode': img})


def upload_cardapio(request):
    print(request.FILE.get('cardapio'))

    return HttpResponse('AAAAAAAAAAAA')

def url_cardapio(request):
    logo = ""


    print(request.FILES.get('logo'));

    if request.FILES.get('logo'):
        cardapio = Cardapio()
        cardapio.arquivo = request.FILES.get('logo')
        cardapio.save()
        logo = cardapio

        print("ARQUIVO:",logo.arquivo)


    response = HttpResponse(content_type='application/pdf')
    qr = qrcode.QRCode(
        version=2,
        box_size=15,
        border=4
    )

    data = request.POST.get('url_cardapio')
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')
    img.save('/home/praciano123/praciano123.pythonanywhere.com/static/img/pdf.png')

    imagem = '/home/praciano123/praciano123.pythonanywhere.com/static/img/pdf.png'

    existing_pdf = PdfFileReader("/home/praciano123/praciano123.pythonanywhere.com/media/modelo/cardapio_modelo_link.pdf")


    buffer = BytesIO()

    pagesize = landscape(A4)
    codigo = canvas.Canvas(buffer, pagesize=pagesize)
    if logo != "":
        codigo.drawImage(ImageReader(logo.arquivo), 90, 460, 75, 75)
        codigo.drawImage(ImageReader(logo.arquivo), 510, 460, 75, 75)


    codigo.drawImage(ImageReader(imagem), 228, 182, 105,105)
    codigo.drawImage(ImageReader(imagem), 650, 182, 105, 105)


    story = []
    text_cidade = []


    f = Frame(2, 20, 25, 100, showBoundary=0)
    cidade = Frame(40, 170, 600, 40, showBoundary=0)

    f.addFromList(story, codigo)
    cidade.addFromList(text_cidade, codigo)
    codigo.save()

    buffer.seek(0)
    name = PdfFileReader(buffer)

    buffer = BytesIO()

    verso = canvas.Canvas(buffer, pagesize=pagesize)

    verso.save()
    buffer.seek(0)

    qrcodes = PdfFileReader(buffer)
    output = PdfFileWriter()

    for i in xrange(existing_pdf.getNumPages()):
        page = existing_pdf.getPage(i)
        if not i:
            page.mergePage(name.getPage(0))
        if i == 1:
            page.mergePage(qrcodes.getPage(0))
        output.addPage(page)
    outputStream = BytesIO()
    output.write(outputStream)
    buffer.close()
    response.write(outputStream.getvalue())
    outputStream.close()

    # response['Content-Disposition'] = 'attachment; filename="cardapio_gerado.pdf"'

    return response
