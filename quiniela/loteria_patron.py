import pandas as pd
import matplotlib.pyplot as plt

# Cargar el archivo Excel con pandas
archivo = 'historico_loteria.xlsx'  # Cambia a la ruta de tu archivo Excel
df = pd.read_excel(archivo)

# Ver las primeras filas del DataFrame para asegurarnos de que se ha cargado correctamente
print(df.head())

# Inicializar el contador de secuencias consecutivas
secuencias_consecutivas = 0

# Recorrer cada fila para identificar secuencias consecutivas
for index, row in df.iterrows():
    # Ordenar la combinación de números en orden ascendente
    combinacion = sorted([row['#1'], row['#2'], row['#3'], row['#4'], row['#5'], row['#6']])
    
    # Buscar secuencias consecutivas
    for i in range(1, len(combinacion)):
        if combinacion[i] == combinacion[i-1] + 1:
            secuencias_consecutivas += 1

# Mostrar el resultado
print(f'Cantidad de secuencias consecutivas encontradas: {secuencias_consecutivas}')

# Si quieres saber cuántas veces se repiten secuencias consecutivas (por ejemplo, 1-2, 3-4, etc.)
# Podemos contar las secuencias específicas
secuencias_especificas = []
for index, row in df.iterrows():
    combinacion = sorted([row['#1'], row['#2'], row['#3'], row['#4'], row['#5'], row['#6']])
    for i in range(1, len(combinacion)):
        if combinacion[i] == combinacion[i-1] + 1:
            secuencia = f'{combinacion[i-1]}-{combinacion[i]}'
            secuencias_especificas.append(secuencia)

# Contar cuántas veces aparece cada secuencia consecutiva
secuencias_contadas = pd.Series(secuencias_especificas).value_counts()

# Mostrar las secuencias más comunes
print(f'Frecuencia de secuencias consecutivas:')
print(secuencias_contadas)

# Graficar las secuencias más comunes
plt.figure(figsize=(10, 6))
secuencias_contadas.head(10).plot(kind='bar', color='skyblue')
plt.title('Frecuencia de Secuencias Consecutivas en la Lotería Primitiva')
plt.xlabel('Secuencia Consecutiva')
plt.ylabel('Frecuencia')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


