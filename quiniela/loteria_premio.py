import pandas as pd
import random

# Cargar el archivo Excel con pandas
archivo = 'historico_loteria.xlsx'  # Cambia a la ruta de tu archivo Excel
df = pd.read_excel(archivo)

# Ver las primeras filas del DataFrame para asegurarnos de que se ha cargado correctamente
print(df.head())

# Extraer todos los números de las columnas #1 a #6 en una lista
numeros = []
for index, row in df.iterrows():
    numeros.extend([row['#1'], row['#2'], row['#3'], row['#4'], row['#5'], row['#6']])

# Convertir la lista de números a un objeto Series de pandas
numeros_series = pd.Series(numeros)

# Filtrar números impares y bajos (1-24)
numeros_bajos_impares = [num for num in range(1, 25) if num % 2 != 0]
# Filtrar números pares y altos (mayores de 24)
numeros_altos_pares = [num for num in range(25, 51) if num % 2 == 0]  # Puedes ajustar el rango si quieres más números altos

# Calcular la frecuencia de aparición de estos números
frecuencia_bajos_impares = numeros_series[numeros_series.isin(numeros_bajos_impares)].value_counts()
frecuencia_altos_pares = numeros_series[numeros_series.isin(numeros_altos_pares)].value_counts()

# Mostrar la frecuencia de aparición de los números bajos impares y altos pares
print(f'Frecuencia de aparición de los números bajos impares:')
print(frecuencia_bajos_impares)
print(f'Frecuencia de aparición de los números altos pares:')
print(frecuencia_altos_pares)

# Identificar los números bajos impares con menor frecuencia
min_frecuencia_bajos = frecuencia_bajos_impares.min()  # Encontrar la frecuencia más baja
numeros_bajos_menos_frecuentes = frecuencia_bajos_impares[frecuencia_bajos_impares == min_frecuencia_bajos].index.tolist()

# Identificar los números altos pares con mayor frecuencia
max_frecuencia_altos = frecuencia_altos_pares.max()  # Encontrar la frecuencia más alta
numeros_altos_mas_frecuentes = frecuencia_altos_pares[frecuencia_altos_pares == max_frecuencia_altos].index.tolist()

# Si hay menos de 4 números con la frecuencia más baja de los bajos impares, completamos con los próximos más bajos
if len(numeros_bajos_menos_frecuentes) < 4:
    otros_bajos_impares = list(set(numeros_bajos_impares) - set(numeros_bajos_menos_frecuentes))
    random.shuffle(otros_bajos_impares)
    # Completar hasta 4 con los siguientes números más bajos
    numeros_bajos_menos_frecuentes.extend(otros_bajos_impares[:4 - len(numeros_bajos_menos_frecuentes)])

# Si hay menos de 2 números altos pares con alta frecuencia, completamos con los más comunes
if len(numeros_altos_mas_frecuentes) < 2:
    otros_altos_pares = list(set(numeros_altos_pares) - set(numeros_altos_mas_frecuentes))
    random.shuffle(otros_altos_pares)
    # Completar hasta 2 con los números altos más comunes
    numeros_altos_mas_frecuentes.extend(otros_altos_pares[:2 - len(numeros_altos_mas_frecuentes)])

# Combinamos los números bajos impares con los altos pares para una combinación de 6 números
combinacion_final = sorted(numeros_bajos_menos_frecuentes[:4] + numeros_altos_mas_frecuentes[:2])

# Mostrar la combinación resultante
print(f'Combinación propuesta de números:')
print(combinacion_final)


