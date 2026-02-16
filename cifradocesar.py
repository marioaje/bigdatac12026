
def funcionCifrarCesar(mensaje):
    print(mensaje)
    desplazamiento = 3
    alfabeto = "abcdefghijklmnopqrstuvwxyz"    #26
               #0123456789 
    resultado =""
    for itemLetra in mensaje:
        print(itemLetra)
        obtenemosPosicion = alfabeto.index(itemLetra)
        print(obtenemosPosicion)
        nuevaPosicion = obtenemosPosicion + desplazamiento 

        if nuevaPosicion >= 26:
            nuevaPosicion = nuevaPosicion - 26

        resultado +=  alfabeto[nuevaPosicion]           

    return resultado 

mensaje = "holaz"
print(mensaje)
print(funcionCifrarCesar(mensaje))