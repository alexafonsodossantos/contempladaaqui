import locale
import requests
from bs4 import BeautifulSoup
import re
class Cotas:
    url = ""
    carta = ""
    credito = 0
    entrada = 0
    parcelas = []
    segmento = "Imóveis"
    vencimento = ""
    codigo = 0




class Parcelas:
    qt_parcelas = 0
    valor_parcelas = 0.0

    def __str__(self):
        return str(self.qt_parcelas) + " x " + str(self.valor_parcelas)


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

for c in chunks:
    cota = Cotas()

    administradora =  c[3][0]
    print("Administradora: ", administradora)
    cota.administradora = administradora

    credito =  int(re.sub('\D','',c[0][0]))/100
    print("Crédito: ", credito)
    cota.credito = credito

    entrada =   (int(re.sub('\D','',c[1][0]))/100) + (credito * 0.07)
    print("Entrada: ", entrada)
    cota.entrada = entrada

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
    
    print("Parcelas:")
    for h in parcelas:
        p = Parcelas()
        p.qt_parcelas = h[0]
        p.valor_parcelas = h[1]
        print(p)

    print("="*80)










