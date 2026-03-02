import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns #libreria de estadisticas

#cargar mi archivo
df = pd.read_csv("FOOD_DATA_GROUP.csv")

#como visualizo las filas?
print(df.head())

#Limpieza datos(elimina la desinformacion, datos ruidosos)
df = df.drop(columns=["Columna1", "Columna2"], errors="ignore")

#como visualizo las filas despues del drop
print(df.isnull().sum())

#funcion de eliminar valor nulos
df = df.dropna()

correlacion = df.select_dtypes(include="number").corr(method="pearson")
print(correlacion)

plt.figure(figsize=(10,8))

sns.heatmap(correlacion, 
            annot=True,
            fmt = ".2f",
            cmap="coolwarm",
            linewidths=0.5)

plt.title("Matriz de datos de correlacion - Pearson")
plt.show()