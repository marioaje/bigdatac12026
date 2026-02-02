# print("Hola clase.")


# #Comentarios son para dejar informacion o explicar
# #Variables, es el algo que cambia en el tiempo o en la ejecuccion
# edad = 40
# edades = 44
# precio = 12.56
# precios = 1000.6
# nombre = "Mario"
# nombres = "Mario"
# apellidos = "Jimenez"
# activo = True
# activos = False


# print(edad)
# print(precio)
# print(nombres)
# print(activo)
# print(activos)
# print(edades)
# print(nombre)


# #Concatenando variable + variable
# print(nombre, apellidos)
# print(nombre + " " + apellidos)
# #version pro
# print ( f"Nombre: {nombre}")


# #Operaciones aritmetica
# resultadoResta = 10 - 8 
# resultadoSuma = 10 + 8 
# resultadoMultiplicar = 10 * 8 
# resultadoDividir = 10 / 8 

# print("resultadoResta", resultadoResta)
# print("resultadoSuma", resultadoSuma)
# print("resultadoMultiplicar", resultadoMultiplicar)
# print("resultadoDividir", resultadoDividir)


# #funcion input, sirve para capturar los datos desde el terminal
# numero = input("Ingrese un numero ")
# texto = input("Ingrese un texto ")

# print("Su numero", numero)
# print("Su texto", texto)


# #Operaciones aritmetica
#el int, es una funcion para convertir el texto en numeros enteros

# numeroUno = int ( input("Ingrese un numero: ") )
# numeroDos = int ( input("Ingrese un numero: ") )

#float, es una funcion para convertir el texto en numeros en decimales
# numeroUno = float ( input("Ingrese un numero: ") )
# numeroDos = float ( input("Ingrese un numero: ") )



# resultadoResta = numeroUno - numeroDos 
# resultadoSuma = numeroUno + numeroDos 
# resultadoMultiplicar = numeroUno * numeroDos
# resultadoDividir = numeroUno / numeroDos

# print("resultadoResta", resultadoResta)
# print("resultadoSuma", resultadoSuma)
# print("resultadoMultiplicar", resultadoMultiplicar)
# print("resultadoDividir", resultadoDividir)


#Condicionales
# edadMario = int ( input("Ingrese la edad base a comparar") )
# edadIsaac = int (input("Ingrese la edad segunda a comparar") )

# #Condicion es el if, el permite validar si o no
# if edadMario > edadIsaac:
#     print("Mario es mayor")
# else:    
#     print("Isaac es mayor")

#Arreglos o listas
# numeros = [1,2,3,4,5,56,6]
# nombres = ["Mario", "Alberto", "Isaac"]
# print(numeros)
# numeros.append(500)#Funcion para agregar un nuevo valor, 
# #todo lo que est adentro del parentesis son parametros
# print(numeros)
# numeros.remove(1)
# print(numeros)
# print(nombres)
#def se usa para indicar que estoy creando una funcion

def contadorDeLetras(parametros):
    #el return sirve para regresarme dato o datos
    return len(parametros)


def suma (datoa, datob):
    return datoa + datob

def resta (datoa, datob):
    return datoa - datob

def multiplica (datoa, datob):
    return datoa * datob

def divide (datoa, datob):
    return datoa / datob


print ( "La operacion de suma es:", suma(32, 23)  )
print ( "La operacion de resta es:", resta(32, 23)  )
print ( "La operacion de multiplica es:", multiplica(32, 23)  )
print ( "La operacion de divide es:", divide(32, 23)  )

print ( contadorDeLetras("mario") )

