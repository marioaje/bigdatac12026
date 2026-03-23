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

print("\nh2") #\n salto de linea es equivalente a dar un enter
print(soup.find("h2").text)



print("\nProductos y h3") #\n salto de linea es equivalente a dar un enter
listaproductos = soup.find_all("div", class_="producto")

for itmeproducto in listaproductos:
    nombre = itmeproducto.find("h3").text
    precio = itmeproducto.find("p").text
    print("\nNombre: ", nombre, " precio: ", precio)


print("\nOpiniones:") #\n salto de linea es equivalente a dar un enter
listaopiniones = soup.find_all("li")

for itmeopiniones in listaopiniones:
    print( "-" ,itmeopiniones.text )
    
# print(soup.find("h3").text)


    

#     <p class="descripcion">Las mejores galletas del país.</p>

    

#     <div class="producto">
#         <h3>Galleta Chocolate</h3>
#         <p class="precio">Precio: 1200</p>
#     </div>

#     <div class="producto">
#         <h3>Galleta Vainilla</h3>
#         <p class="precio">Precio: 1000</p>
#     </div>

#     <div class="producto">
#         <h3>Galleta Fresa</h3>
#         <p class="precio">Precio: 1100</p>
#     </div>

#     <h2>Opiniones</h2>

#     <ul>
#         <li class="opinion">Muy ricas</li>
#         <li class="opinion">Excelente sabor</li>
#         <li class="opinion">No me gustaron</li>
#     </ul>

#     <h2>Tabla de información</h2>

#     <table border="1">
#         <tbody><tr>
#             <th>Producto</th>
#             <th>Calorías</th>
#         </tr>
#         <tr>
#             <td>Chocolate</td>
#             <td>250</td>
#         </tr>
#         <tr>
#             <td>Vainilla</td>
#             <td>200</td>
#         </tr>
#     </tbody></table>

#     <a href="https://example.com">Visitar tienda</a>


# </body>