import re
import json
from urllib.request import urlopen

url = "https://ipinfo.io/json"

resposta = urlopen(url)

dados = json.load(resposta)

ip = dados['ip']
org = dados['org']
cidade = dados['city']
pais = dados['country']
regiao = dados['region']

print(f"IP: {ip} Organização: {org} Cidade: {cidade} País: {pais} Região: {regiao}")
