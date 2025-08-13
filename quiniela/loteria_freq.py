import pandas as pd

# Cargar el archivo Excel con pandas
archivo = 'historico_loteria.xlsx'  # Cambia a la ruta de tu archivo Excel
df = pd.read_excel(archivo)

# Ver las primeras filas para asegurarnos de que se haya cargado correctamente
print(df.head())

# Crear una lista para almacenar las combinaciones de los 6 números principales
combinaciones = []

# Recorrer todas las filas y extraer las combinaciones de los 6 números principales
for index, row in df.iterrows():
    combinacion = tuple(sorted([row['#1'], row['#2'], row['#3'], row['#4'], row['#5'], row['#6']]))
    combinaciones.append(combinacion)

# Convertir la lista de combinaciones a un objeto Series de pandas
combinaciones_series = pd.Series(combinaciones)

# Contar la frecuencia de cada combinación
frecuencia_combinaciones = combinaciones_series.value_counts().sort_values(ascending=False)

# Mostrar la combinación que más se ha repetido
print(f"La combinación más frecuente es: {frecuencia_combinaciones.index[0]}")
print(f"Se ha repetido {frecuencia_combinaciones.iloc[0]} veces.")



