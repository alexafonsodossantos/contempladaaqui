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
# Create your views here.


def update_agent(request):
    if request.user.is_authenticated:
        try:
            latest_cod = int(Cota.objects.all().aggregate(Max('codigo'))['codigo__max']) + 1
        except:
            latest_cod = 14000

        Cota.objects.all().delete()
        class Cotas:
            url = ""
            carta = ""
            credito = 0
            entrada = 0
            parcelas = ""
            segmento = ""
            vencimento = ""
            codigo = 0


        locale.setlocale(locale.LC_MONETARY, "pt_BR.UTF-8")
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:55.0) Gecko/20100101 Firefox/55.0',
        }

        html_content = requests.get("https://contempladoschapeco.com.br/consorcio/imovel/", headers=headers).text
        soup = BeautifulSoup(html_content,features="html.parser")
        lista_maior = []
        obj_list = []

        table = soup.find_all('table')
        tds = soup.find_all('td')

        for a in tds:
            data = a.contents
            lista_maior.append(data)

        chunks = [lista_maior[x:x+6] for x in range(0, len(lista_maior), 6)]

        for a in chunks:
            index = chunks.index(a)
            obj = Cotas()
            credito =  int(re.sub('\D','',a[0][0]))/100
            entrada =   (int(re.sub('\D','',a[1][0]))/100) + (credito * 0.07)
            try:
                parcelas =  a[2][0] + " " + a[5][0]
            except:
                parcelas =  a[2][0]
            finally:
                administradora =  a[3][0]
                vencimento = "Dia " + a[4][0][0:2]

            obj.credito = credito
            obj.carta = administradora
            obj.entrada = entrada
            obj.parcelas = parcelas
            obj.vencimento = vencimento

            if administradora == "Caixa":
                obj.url = "https://www.contempladaaqui.com.br/wp-content/uploads/2021/05/caixa.png"
            elif administradora == "Bradesco":
                obj.url = "https://www.contempladaaqui.com.br/wp-content/uploads/2021/07/Bradesco.png"
            elif administradora == "Itau":
                obj.url = "https://www.contempladaaqui.com.br/wp-content/uploads/2021/07/Itau.png"
            elif administradora == "Caixa | SX5":
                obj.url = "https://www.contempladaaqui.com.br/wp-content/uploads/2021/05/caixa.png"
            else:
                obj.url = ""
            obj.segmento = "Imóveis"
            obj.codigo  = latest_cod + index
            obj.credito = locale.currency(obj.credito, grouping=True)
            obj.entrada = locale.currency(obj.entrada, grouping=True)
            obj_list.append(obj)

        for a in obj_list:
            cota = Cota.objects.create(codigo = a.codigo, administradora = a.carta,
            valor = a.credito, entrada = a.entrada, parcelas = a.parcelas, segmento = a.segmento, vencimento = a.vencimento, img = a.url  )
            print('valor inserido.')

        latest_cod = int(Cota.objects.all().aggregate(Max('codigo'))['codigo__max'])
        print(latest_cod)


        html_content = requests.get("https://contempladoschapeco.com.br/consorcio/veiculo/", headers=headers).text
        soup = BeautifulSoup(html_content,features="html.parser")
        lista_maior = []
        obj_list = []

        table = soup.find_all('table')
        tds = soup.find_all('td')

        for a in tds:
            data = a.contents
            lista_maior.append(data)

        chunks = [lista_maior[x:x+6] for x in range(0, len(lista_maior), 6)]

        for a in chunks:
            index = chunks.index(a)
            obj = Cotas()
            credito =  int(re.sub('\D','',a[0][0]))/100
            entrada =   (int(re.sub('\D','',a[1][0]))/100) + (credito * 0.07)
            try:
                parcelas =  a[2][0] + " " + a[5][0]
            except:
                parcelas =  a[2][0]
            finally:
                administradora =  a[3][0]
                vencimento = "Dia " + a[4][0][0:2]

            obj.credito = credito
            obj.carta = administradora
            obj.entrada = entrada
            obj.parcelas = parcelas
            obj.vencimento = vencimento

            if administradora == "Caixa":
                obj.url = "https://www.contempladaaqui.com.br/wp-content/uploads/2021/05/caixa.png"
            elif administradora == "Bradesco":
                obj.url = "https://www.contempladaaqui.com.br/wp-content/uploads/2021/07/Bradesco.png"
            elif administradora == "Itau":
                obj.url = "https://www.contempladaaqui.com.br/wp-content/uploads/2021/07/Itau.png"
            elif administradora == "Caixa | SX5":
                obj.url = "https://www.contempladaaqui.com.br/wp-content/uploads/2021/05/caixa.png"
            else:
                obj.url = ""
            obj.segmento = "Automóveis"
            obj.codigo  = latest_cod + index
            obj.credito = locale.currency(obj.credito, grouping=True)
            obj.entrada = locale.currency(obj.entrada, grouping=True)
            obj_list.append(obj)

        for a in obj_list:
            cota = Cota.objects.create(codigo = a.codigo, administradora = a.carta,
            valor = a.credito, entrada = a.entrada, parcelas = a.parcelas, segmento = a.segmento, vencimento = a.vencimento, img = a.url  )
            print('valor inserido.')

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
    queryset = Cota.objects.all()
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