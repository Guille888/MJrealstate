import pandas as pd

# Cargar el archivo Excel con pandas
archivo = 'historico_loteria.xlsx'  # Cambia a la ruta de tu archivo Excel
df = pd.read_excel(archivo)

# Ver las primeras filas del DataFrame para asegurarnos de que se ha cargado correctamente
print(df.head())

# Calcular la frecuencia de aparición de los números de reintegro (columna 'R')
frecuencia_reintegro = df['R'].value_counts()

# Mostrar la frecuencia de aparición de los números de reintegro
print(f'Frecuencia de aparición de los números de reintegro:')
print(frecuencia_reintegro)
