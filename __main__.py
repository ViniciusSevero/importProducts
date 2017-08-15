# -*- coding: utf-8 -*-
import sys
import os
import requests
import json

services = (
    {"categoria": "maquiagem", "url": "http://rede.natura.net/espaco/c/maquiagem/u/N-1mf4ph0?No=%(page)s&json=true"},
    {"categoria": "perfumaria", "url": "http://rede.natura.net/espaco/c/perfumaria/u/N-1ukkhi8?No=%(page)s&json=true"},
    {"categoria": "gerais", "url": "http://rede.natura.net/espaco/c/gerais/achados-da-natura/u/N-1vcnasl?No=%(page)s&json=true"},
    {"categoria": "promocoes", "url": "http://rede.natura.net/espaco/c/promocoes/u/N-ul5m3b?No=%(page)s&json=true"},
    {"categoria": "presentes", "url": "http://rede.natura.net/espaco/c/presentes/u/N-ntmbow?No=%(page)s&json=true"},
    {"categoria": "lancamentos", "url": "http://rede.natura.net/espaco/c/lancamentos/u/N-13emn1s?No=%(page)s&json=true"},
    {"categoria": "infantil", "url": "http://rede.natura.net/espaco/c/infantil/u/N-ycky2i?No=%(page)s&json=true"},
    {"categoria": "homem", "url": "http://rede.natura.net/espaco/c/homem/u/N-celrxd?No=%(page)s&json=true"},
    {"categoria": "corpo", "url": "http://rede.natura.net/espaco/c/corpo-e-banho/u/N-1oau59a?No=%(page)s&json=true"},
    {"categoria": "rosto", "url": "http://rede.natura.net/espaco/c/rosto/u/N-1cbzq9?No=%(page)s&json=true"},
    {"categoria": "cabelos", "url": "http://rede.natura.net/espaco/c/cabelos/u/N-fzmx1z?No=%(page)s&json=true"}
)

def main(argv):
    for item in services:
        arr = []
        for i in range(1,200):
            url = str(item["url"]) % {"page": i}
            print("GET na url %s" % url)
            result = requests.get(url)
            print("Status code %d" % result.status_code)
            aux = json.loads(result.text)["dataLayerGTM"]["productList"]
            if len(aux) == 0:
                break;
            for product in aux:
                product["description"] = getDescription(product["id"])
            arr += aux
        writeFile(item["categoria"], str(arr))
    print("FIm da execução")

def writeFile(file, text):
    print("Salvando arquivo %s" % file)
    file = os.path.dirname(os.path.realpath(__file__)) + ("/%s.txt" % file)
    f = open(file, 'w+', encoding='utf-8')
    f.write('%s \n' % text)
    f.close()

def getDescription(id):
    result = requests.post('http://rede.natura.net/cartridges/RecordDetailsPage/productInitialModule/json/product-json.jsp', data = {'productId': id})
    return result.text

if __name__ == "__main__":
    main(sys.argv)