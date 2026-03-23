import requests
from bs4 import BeautifulSoup

url = "https://paginas-web-cr.com/profeMario/pagina_avanzada.html"

#obtener la pagina web
respuesta = requests.get(url)
#conversion html a un objeto
soup = BeautifulSoup(respuesta.text, "html.parser")

#Los productos
print("\nProductos") #\n salto de linea es equivalente a dar un enter
listaproductos = soup.find_all("div", class_="producto")

for itmeproducto in listaproductos:
    nombre = itmeproducto.find("h3").text
    precio = itmeproducto.find("p", class_="precio").text
    calorias = itmeproducto.find("p",  class_="calorias").text
    categoria = itmeproducto['data-categoria']
    print("\nNombre: ", nombre, " --- precio: ", precio, " --- calorias: ", calorias, " --- calcategoriaorias: ", categoria)

# <!-- ===================== -->
# <!-- PRODUCTOS -->
# <!-- ===================== -->
# <h2>Productos</h2>

# <div class="producto" data-categoria="Chocolate">
#     <h3>Galleta Chocolate</h3>
#     <p class="precio">1200</p>
#     <p class="calorias">250</p>
#     <span class="stock">Disponible</span>
# </div>

# <div class="producto" data-categoria="Vainilla">
#     <h3>Galleta Vainilla</h3>
#     <p class="precio">1000</p>
#     <p class="calorias">200</p>
#     <span class="stock">Agotado</span>
# </div>

# <div class="producto" data-categoria="Frutales">
#     <h3>Galleta Fresa</h3>
#     <p class="precio">1100</p>
#     <p class="calorias">210</p>
#     <span class="stock">Disponible</span>
# </div>

# <div class="producto" data-categoria="Chocolate">
#     <h3>Galleta Doble Chocolate</h3>
#     <p class="precio">1500</p>
#     <p class="calorias">300</p>
#     <span class="stock">Disponible</span>
# </div>
