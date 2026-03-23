import requests
from bs4 import BeautifulSoup

url = "https://paginas-web-cr.com/profeMario/pagina_prueba.html"

#obtener la pagina web
respuesta = requests.get(url)


#doble check, verifica si la pagina tiene informacion y se cargo
print("Estado: ", respuesta.status_code )

#conversion html a un objeto
soup = BeautifulSoup(respuesta.text, "html.parser")

#Leer lo que tiene la pagina 
print("\nTitulo") #\n salto de linea es equivalente a dar un enter
print(soup.title.text)

#encabezado
print("\nh1") #\n salto de linea es equivalente a dar un enter
print(soup.find("h1").text)