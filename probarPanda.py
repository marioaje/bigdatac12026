import pandas as nombreDeMiProcesoPandas

archivo = nombreDeMiProcesoPandas.read_csv('Personas.csv')

archivo.head()#primeras filas
# archivo.info()#tipos de datos
# archivo.describe()#estadisticas

# Nombre,Edad,Provincia

#archivo['Provincia'].value_counts().plot(kind='bar', title='Resumen')

contadorProvincia = archivo['Provincia'].value_counts()
mayoresEdad = archivo[ archivo['Edad'] >= 40 ]
print(mayoresEdad)

# print(archivo['Provincia'])
# print(contadorProvincia)
# print(archivo['Edad'])