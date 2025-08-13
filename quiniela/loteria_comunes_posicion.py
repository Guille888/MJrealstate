import pandas as pd

# Cargar el archivo Excel con pandas
archivo = 'historico_loteria.xlsx'  # Cambia a la ruta de tu archivo Excel
df = pd.read_excel(archivo)

# Ver las primeras filas para asegurarnos de que se haya cargado correctamente
print(df.head())

# Crear diccionarios para contar la frecuencia de cada número en cada posición
frecuencia_posiciones = {
    '#1': {},
    '#2': {},
    '#3': {},
    '#4': {},
    '#5': {},
    '#6': {}
}

# Recorrer todas las filas y contar cuántas veces aparece cada número en cada posición
for index, row in df.iterrows():
    for i, col in enumerate(['#1', '#2', '#3', '#4', '#5', '#6']):
        numero = row[col]
        if numero in frecuencia_posiciones[col]:
            frecuencia_posiciones[col][numero] += 1
        else:
            frecuencia_posiciones[col][numero] = 1

# Mostrar las frecuencias de los números más comunes por posición
for pos in frecuencia_posiciones:
    print(f"Posición {pos}:")
    # Ordenar los números por frecuencia (de mayor a menor)
    ordenados = sorted(frecuencia_posiciones[pos].items(), key=lambda x: x[1], reverse=True)
    for numero, frecuencia in ordenados[:10]:  # Mostrar los 10 números más frecuentes
        print(f"  Número {numero}: {frecuencia} veces")
    print()  # Salto de línea para separar las posiciones
