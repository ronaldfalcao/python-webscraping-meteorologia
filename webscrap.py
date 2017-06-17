#webscraping com Python utilizando o BeautifulSoup utilizando as buscas da biblioteca

import requests

from bs4 import BeautifulSoup

page = requests.get("http://dataquestio.github.io/web-scraping-pages/simple.html")
soup = BeautifulSoup(page.content, 'html.parser')

##Retornando o conteúdo da tag <p>
#print (soup.find_all('p'))

##Exibindo apenas o conteúdo da tag <p>
#print (soup.find_all('p')[0].get_text())

##Alterando a página para buscas com id e class
page = requests.get("http://dataquestio.github.io/web-scraping-pages/ids_and_classes.html")
soup = BeautifulSoup(page.content, 'html.parser')

##Exbindo a tag <p> com class específico "outer-text"
#print(soup.find_all('p', class_='outer-text'))

##Exibindo qualquer tag com class "outer-text"
#print(soup.find_all(class_="outer-text"))

##Exibindo por um id específico "first"
#print(soup.find_all(id="first"))

##Exibindo com busca pelos seletores CSS
print(soup.select("div p"))
