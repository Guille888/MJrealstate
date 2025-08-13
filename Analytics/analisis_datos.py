import pandas as pd
import matplotlib.pyplot as plt

# Leer datos de un archivo Excel
print("Leyendo datos del archivo Excel...")
data = pd.read_excel('datos.xlsx')
print("Datos leídos exitosamente.")

# Mostrar los nombres de las columnas para verificar
print("Nombres de las columnas en el DataFrame:")
print(data.columns)

# Mostrar los primeros registros para verificar
print("Primeros registros de los datos:")
print(data.head())

# Calcular la media de los valores
media_valores = data['Value'].mean()
print(f"La media de los valores es: {media_valores}")

# Dibujar la media en el gráfico
plt.axhline(y=media_valores, color='r', linestyle='--', label='Media')
plt.legend()

# Crear un gráfico de barras
print("Creando gráfico de barras...")
plt.bar(data['Category'], data['Value'])
plt.xlabel('Categoría')
plt.ylabel('Valor')
plt.title('Gráfico de Barras')
print("Mostrando gráfico de barras...")
plt.show()