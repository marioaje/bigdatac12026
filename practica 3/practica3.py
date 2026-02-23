# Cargue el archivo nhanes_2015_2016.csv en un dataFrame y
#  realice las siguientes exploraciones
#  1. Usando la variable de estado civil [DMDMARTL](https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/2015/DataFiles/DEMO_I.htm#DMDMARTL) 
# agregue una nueva columna al dataFrame llamada "EstadoCivil" con los valores 
# descriptivos para que tenga etiquetas informativas. 
# 1. Usando la variable RIAGENDR agregue una nueva columna al dataFrame llamada 
# "Genero"con los valores descriptivos "Male" y "Female" (como lo hicimos en clases). 
# 1. Restringiendo la muestra a la población femenina, estratifique a los sujetos en franjas
#  de edad de diez años y construya la distribución del estado civil dentro de cada franja de edad.
#  Presente la distribución en términos de proporciones que deben sumar 
# 1. (Como lo hicimos al final de la clase al comparar grupos de edad con el nivel de educación).
# 1. Hacer lo mismo para la población masculina. 
# 1. Construir histogramas separados para las alturas de mujeres y hombres usando la variable BMXHT
# 1. Construir un diagrama de caja (box plot) que muestre las alturas de mujeres y hombres.

import pandas as pd
import matplotlib.pyplot as plt
import os
#Cargar el archivo

df = pd.read_csv(r"d:\Github\New folder\bigdatac12026\practica 3\nhanes_2015_2016.csv")
#df = pd.read_csv("datos/nhanes_2015_2016.csv")
# print(os.getcwd())

# #Veamos las filas
print(df.head())

#  1. Usando la variable de estado civil [DMDMARTL](https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/2015/DataFiles/DEMO_I.htm#DMDMARTL) 
# agregue una nueva columna al dataFrame llamada "EstadoCivil" con los valores 
# descriptivos para que tenga etiquetas informativas. 
#SEQN,ALQ101,ALQ110,ALQ130,SMQ020,RIAGENDR,RIDAGEYR,RIDRETH1,DMDCITZN,DMDEDUC2,DMDMARTL,DMDHHSIZ,WTINT2YR,SDMVPSU,SDMVSTRA,INDFMPIR,BPXSY1,BPXDI1,BPXSY2,BPXDI2,BMXWT,BMXHT,BMXBMI,BMXLEG,BMXARML,BMXARMC,BMXWAIST,HIQ210

#clase o atributos


estado_civil_map = {
    1:"Married",
    2:"Widowed",
    3:"Divorced",
    4:"Separated",
    5:"Never married",
    6:"Living with partner",
    77:"Refused",
    99:"Don't Know"
}

df["EstadoCivil"] = df["DMDMARTL"].map(estado_civil_map)

print(df[["DMDMARTL","EstadoCivil"]].head())

# persona = {
#     codigo:12212
#     nombre:"Mario"
#     cedula:"123"
#     telefono:"6138"
#     correo:"mario"
# }

# 1. Usando la variable RIAGENDR agregue una nueva columna al dataFrame llamada 
# "Genero"con los valores descriptivos "Male" y "Female" (como lo hicimos en clases).
# 
genero_map ={
    1: "Male",
    2: "Female",
    3: "Other"
}

df["Genero"] = df["RIAGENDR"].map(genero_map)

print(df[["RIAGENDR","Genero"]].head())


#Los parentesis, son para llamar funciones, para el envio de parametros
#Los [], para listas, arreglos, caracteristicas
#Los corchetes {}, para creacion de clases, dicionarios, mapas, 
#json, apertura y cierre de una funcion


# 1. Restringiendo la muestra a la población femenina, estratifique a los sujetos
#  en franjas
#  de edad de diez años y construya la distribución del estado civil
#  dentro de cada franja de edad.
#  Presente la distribución en términos de proporciones que deben sumar 

#RIDAGEYR 
df["GrupoEdad"] =  pd.cut( df["RIAGENDR"], bins=range(0,120,10), right=False )


#Filtrar . Restringiendo la muestra a la población femenina
mujeres = df[df["Genero"]=="Female"]


#y construya la distribución del estado civil
dist_mujeres = (   mujeres.groupby("GrupoEdad")["EstadoCivil"].value_counts(normalize=True))

print ("Distribucion de mmujeres", dist_mujeres)



#Filtrar . Restringiendo la muestra a la población femenina
hombres = df[df["Genero"]=="Male"]


#y construya la distribución del estado civil
dist_hombres = (   hombres.groupby("GrupoEdad")["EstadoCivil"].value_counts(normalize=True))

print ("Distribucion de hombres", dist_hombres)


#Histograma
plt.figure()

plt.boxplot([mujeres["BMXHT"].dropna(),hombres["BMXHT"].dropna()])

plt.xticks([1,2], ["mujeres", "hombres"])
plt.ylabel("Altura (cm)")
plt.title("Box de alturas de nhanes_2015_2016")
plt.show()


# 1. Hacer lo mismo para la población masculina. 
# 1. Construir histogramas separados para las alturas de mujeres y hombres
#  usando la variable BMXHT
# 1. Construir un diagrama de caja (box plot)
#  que muestre las alturas de mujeres y hombres.
