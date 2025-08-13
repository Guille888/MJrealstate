import pandas as pd

# Cargar el archivo Excel con pandas
archivo = 'historico_loteria.xlsx'  # Cambia a la ruta de tu archivo Excel
df = pd.read_excel(archivo)

# Ver las primeras filas para asegurarnos de que se haya cargado correctamente
print(df.head())

# Extraer todos los números de las columnas #1 a #6 y agregarlos a una lista
numeros = []
for index, row in df.iterrows():
    numeros.extend([row['#1'], row['#2'], row['#3'], row['#4'], row['#5'], row['#6']])

# Convertir la lista de números a un objeto Series de pandas
numeros_series = pd.Series(numeros)

# Contar la frecuencia de cada número
frecuencia_numeros = numeros_series.value_counts().sort_values(ascending=False)

# Mostrar los números que más veces han salido
print("Frecuencia de los números más comunes:")
print(frecuencia_numeros)
