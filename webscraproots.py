#webscraping com Phyton utilizando o BeautifulSoup (modo roots)

import requests

from bs4 import BeautifulSoup

url = "http://dataquestio.github.io/web-scraping-pages/simple.html"

#Conteúdo sem tratamento...
page = requests.get(url)
#print (page.content)

#Conteúdo tratado...
soup = BeautifulSoup(page.content, 'html.parser')
#print(soup.prettify())

#Retorna na lista as tags superiores e o conteúdo das filhas
#print (list(soup.children))

#Verifica os tipos das tags (usando as tags superiores de exemplo)
#print ([type(item) for item in list(soup.children)])

#Pegando a tag hmtl e suas filhas
html = list(soup.children)[2]
#print (html)

#Pegando o conteúdo body
body = list(html.children)[3]
#print (body)

#Pegando o conteúdo do parágrafo (p) que tem a informação que queremos.
#Usando get_text para retornar apenas o conteúdo sem as tags <p> e </p>.
p = list(body.children)[1]
#print (p.get_text())

#retornando o status da página
if page.status_code != True:
    print ("Erro:",page.status_code)
else:
    print("Página Acessada com Sucesso!");




