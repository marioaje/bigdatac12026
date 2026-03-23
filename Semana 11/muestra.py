import requests
from bs4 import BeautifulSoup

url = "https://paginas-web-cr.com/profeMario/pagina_prueba.html"

#obtener la pagina web
respuesta = requests.get(url)


#doble check, verifica si la pagina tiene informacion y se cargo
print("Estado: ", respuesta.status_code )