import requests
from bs4 import BeautifulSoup

url = "https://paginas-web-cr.com/profeMario/pagina_regex.html"

#obtener la pagina web
respuesta = requests.get(url)
#conversion html a un objeto
soup = BeautifulSoup(respuesta.text, "html.parser")

#La idea es Buscar, Correos, Telefonos, Fechas, URL