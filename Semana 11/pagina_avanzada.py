import requests
from bs4 import BeautifulSoup

url = "https://paginas-web-cr.com/profeMario/pagina_avanzada.html"

#obtener la pagina web
respuesta = requests.get(url)

#Los productos


