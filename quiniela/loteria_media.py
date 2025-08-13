import pandas as pd
import matplotlib.pyplot as plt

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
frecuencia_numeros = numeros_series.value_counts()

# Calcular la media de veces que ha salido cada número
total_sorteos = len(df)
media = frecuencia_numeros / total_sorteos

# Verificar las primeras frecuencias y medias
print("Frecuencia de cada número:")
print(frecuencia_numeros.head())
print("\nMedia de veces que ha salido cada número:")
print(media.head())

# Graficar los resultados ordenados de menor a mayor
if not media.empty:
    plt.figure(figsize=(10, 6))
    media.sort_values(ascending=True).plot(kind='bar', color='skyblue')  # Ordenado de menor a mayor
    plt.title('Media de veces que ha salido cada número en la Lotería Primitiva')
    plt.xlabel('Número')
    plt.ylabel('Media de veces')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
else:
    print("No hay datos válidos para graficar.")


