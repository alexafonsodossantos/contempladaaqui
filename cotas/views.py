from django.shortcuts import render
from .models import Cota, Parcelas
import locale
import re
import requests
from bs4 import BeautifulSoup
from django.http import HttpResponse, JsonResponse
from django.template import loader
from django.db.models import Avg, Max, Min, Sum
from django.views.generic.list import ListView
import json
from .serializers import CotaSerializer, ParcelasSerializer
from rest_framework import generics
from django.shortcuts import get_object_or_404, redirect
from PIL import Image, ImageFont, ImageDraw
# Create your views here.

locale.setlocale(locale.LC_MONETARY, "pt_BR.UTF-8")
def update_agent(request):
    if request.user.is_authenticated:
        latest_cod = 15000

        #Cota.objects.all().delete()



        locale.setlocale(locale.LC_MONETARY, "pt_BR.UTF-8")
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:55.0) Gecko/20100101 Firefox/55.0',
        }

        html_content = requests.get("https://contempladoschapeco.com.br/consorcio/imovel/", headers=headers).text
        soup = BeautifulSoup(html_content,features="html.parser")
        lista_maior = []

        table = soup.find_all('table')
        tds = soup.find_all('td')

        for a in tds:
            data = a.contents
            lista_maior.append(data)

        chunks = [lista_maior[x:x+6] for x in range(0, len(lista_maior), 6)]

        for c in chunks:
            cota = Cota()
            segmento = "Imóveis"
            codigo = latest_cod + 1
            cota.codigo = codigo
            print("Código: ", codigo)

            administradora =  c[3][0]
            print("Administradora: ", administradora)
            cota.administradora = administradora

            credito =  float(re.sub('\D','',c[0][0]))/100
            print("Crédito: ", credito)
            cota.credito = credito

            entrada =   float(re.sub('\D','',c[1][0]))/100 + (credito * 0.07)
            print("Entrada: ", entrada)
            cota.entrada = entrada
            vencimento = int(c[4][0][0:2])
            parcelas_str =  c[2][0]
            parcelas_list = parcelas_str.rsplit(" ")

            new_list = []
            for b in parcelas_list:
                c = re.sub('\D','',b)
                if c != "":
                    new_list.append(int(c))
                
            for d in new_list:
                i = new_list.index(d)

                if i % 2 != 0:
                    new_list[i] = d / 100
                
                parcelas = [new_list[x:x+2] for x in range(0, len(new_list), 2)]
            
            cota = Cota.objects.create(codigo = codigo,
                                        administradora = administradora,
                                        valor = credito, 
                                        entrada = entrada, 
                                        segmento = segmento, 
                                        vencimento = vencimento
                                        )
            cota.save()
            latest_cod = codigo
            print("Parcelas:")
            for h in parcelas:

                qt_parcelas = h[0]
                valor_parcelas = h[1]

                pcl = Parcelas.objects.create(cota_id = cota, qt_parcelas = qt_parcelas, valor_parcelas = valor_parcelas)
                pcl.save()

            cota.save()
            print("="*50)
        return HttpResponse("Dados inseridos!")
    else:
        return HttpResponse('Não autorizado.')



def index(request):
    cotas_list = Cota.objects.all()
    template = loader.get_template('index.html')
    total_cotas = cotas_list.count()

        
    context = {
            'cotas_list': cotas_list,
            'total_cotas': total_cotas,
            
    }
    return HttpResponse(template.render(context, request))
    


def dashboard(request):
    if request.user.is_authenticated:

        cotas_list = Cota.objects.all()
        template = loader.get_template('dashboard.html')
        total_cotas = cotas_list.count()

            
        context = {
                'cotas_list': cotas_list,
                'total_cotas': total_cotas,
                
        }
        return HttpResponse(template.render(context, request))
    else:
        return HttpResponse('Não autorizado.')


def dashboard_detail(request, cota_cod):
    if request.user.is_authenticated:
        cota = get_object_or_404(Cota, codigo=cota_cod)
        return render(request, 'cota.html', {'cota': cota})
    else:
        return HttpResponse("Não autorizado.")


def dashboard_create_template(request, pk):
    if request.user.is_authenticated:
        cota = get_object_or_404(Cota, pk=pk)
        

        my_image = Image.open("template_blank.png")
        my_image = my_image.convert('RGBA')
        valor_font = ImageFont.truetype('bebas_neue/BebasNeue-Regular.ttf', 140)
        parcelas_font = ImageFont.truetype('bebas_neue/BebasNeue-Regular.ttf', 35)
        entrada_font = ImageFont.truetype('bebas_neue/BebasNeue-Regular.ttf', 50)

        segmento = "Crédito disponível "+cota.administradora+" - "+cota.segmento
        valor = locale.currency(cota.valor, grouping=True)
        entrada = "Entrada: "+ locale.currency(cota.entrada, grouping=True)
        cota_parcelas = Parcelas.objects.filter(cota_id = pk)

        parcelas = "Parcelas: "

        for a in cota_parcelas:
            parcelas += str(a.qt_parcelas)
            parcelas += "x "
            parcelas += locale.currency(a.valor_parcelas, grouping=True)

            if len(cota_parcelas)>1:
                parcelas += " + "

        image_editable = ImageDraw.Draw(my_image)



        image_editable.text((20,670), segmento, (255,255,255), font=entrada_font)
        #                     X,Y        TEXTO      R  G  B       FONTE
        image_editable.text((20,700), valor, (245,249,13), font=valor_font)

        image_editable.text((20,835), entrada, (255,255,255), font=entrada_font)

        parcelas = parcelas[:-2]

        image_editable.text((20,890), parcelas, (255,255,255), font=parcelas_font)

        my_image.save(str(cota.codigo)+".png")






        file = open(str(cota.codigo)+".png", "rb").read()
        rea_response = HttpResponse(file, content_type='image/png')
        rea_response['Content-Disposition'] = 'attachment; filename={}'.format(str(cota.codigo)+'.jpg')
        return rea_response
    else:
        return HttpResponse("Não autorizado.")


def dashboard_update_cota(request, codigo):
    if request.user.is_authenticated:
        queryset = request.POST
        print(queryset)

        cota_update = Cota.objects.get(codigo = codigo)

        cota_update.administradora = request.POST.get('administradora')
        cota_update.valor = request.POST.get('valor')
        cota_update.entrada = request.POST.get('entrada')
        cota_update.parcelas = request.POST.get('parcelas')
        cota_update.segmento = request.POST.get('segmento')
        cota_update.vencimento = request.POST.get('vencimento')

        cota_update.save()
        
        return redirect('/dashboard')
    else:
        return HttpResponse("Não autorizado.")

def dashboard_remove_cota(request, codigo):
    if request.user.is_authenticated:
        Cota.objects.get(codigo = codigo).delete()
        return redirect('/dashboard')
    else:
        return HttpResponse("Não autorizado.")

class CotaAPIView(generics.ListCreateAPIView):
    queryset = Cota.objects.order_by('id')
    serializer_class = CotaSerializer

class ParcelaAPIView(generics.ListCreateAPIView):
    queryset = Parcelas.objects.all()
    serializer_class = ParcelasSerializer

    #return JsonResponse(cotas_list, safe=False)

    """    cotas_list = {
    "rows": [
    {
      "id": 0,
      "codigo":123,
      "administradora": "teste",
      "valor": 100,
      "parcelas": "10x R$ 10,00",
      "segmento":"Imóveis",
      "vencimento":"Dia 31"
    },
    
    ]}"""