import json
import urllib.request

#Carrega um JSON
url = 'https://sisu-api-pcr.apps.mec.gov.br/api/v1/oferta/instituicao/570'
with urllib.request.urlopen(url) as response:
  resp = response.read()

#Faz a análise desse JSON.
resp = json.loads(resp.decode('utf-8'))

with open('ofertas.csv', 'w') as arquivo:
  #Itera por todos os itens do dicionário principal....
  for k, v in resp.items():
    #...se a have 'co_oferta' está contida no dicionário aninhado...
    if 'co_oferta' in v:      
      print(v['co_oferta'], file=arquivo)         #...se sim, imprime seu valor.