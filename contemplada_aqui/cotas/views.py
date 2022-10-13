from django.shortcuts import render
from .models import Cota
import locale
import re
import requests
from bs4 import BeautifulSoup
from django.http import HttpResponse
from django.template import loader
from django.db.models import Avg, Max, Min, Sum
# Create your views here.


def update_agent(request):
    latest_cod = 14000
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



def index(request):
    cotas_list = Cota.objects.all()
    template = loader.get_template('index.html')
    context = {
        'cotas_list': cotas_list,
    }
    return HttpResponse(template.render(context, request))