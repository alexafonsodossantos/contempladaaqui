import locale
import re
import requests
from bs4 import BeautifulSoup
import mysql.connector


mydb = mysql.connector.connect(
host="bd_cotas.mysql.dbaas.com.br",
user="bd_cotas",
password="Ab742853964",
database="bd_cotas"
)

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

for b in obj_list:
    mycursor = mydb.cursor()
    sql = "INSERT INTO TB_COTAS (ADMINISTRADORA, CARTA, CREDITO, ENTRADA, PARCELAS, SEGMENTO, VENCIMENTO, CODIGO) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
    val = (b.url, b.carta, b.credito, b.entrada, b.parcelas, b.segmento, b.vencimento, b.codigo)
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "usuário cadastrado.")

mycursor = mydb.cursor()
mycursor.execute("SELECT MAX(CODIGO) FROM TB_COTAS ;")
latest_cod = int(mycursor.fetchall()[0][0])


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

for b in obj_list:
    mycursor = mydb.cursor()
    sql = "INSERT INTO TB_COTAS (ADMINISTRADORA, CARTA, CREDITO, ENTRADA, PARCELAS, SEGMENTO, VENCIMENTO, CODIGO) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
    val = (b.url, b.carta, b.credito, b.entrada, b.parcelas, b.segmento, b.vencimento, b.codigo)
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "usuário cadastrado.")