import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix
import matplotlib.pyplot as plt

# Crear un conjunto de datos ficticio
data = {
    'equipo_local': ['A', 'B', 'C', 'D', 'E', 'A', 'B', 'C', 'D', 'E'],
    'equipo_visitante': ['B', 'C', 'D', 'E', 'A', 'C', 'D', 'E', 'A', 'B'],
    'goles_local': [2, 1, 0, 3, 2, 1, 2, 0, 3, 1],
    'goles_visitante': [1, 2, 3, 1, 0, 2, 1, 3, 0, 2],
    'puntos_local': [3, 1, 0, 3, 3, 1, 3, 0, 3, 1],  # 3 puntos por victoria, 1 por empate, 0 por derrota
    'puntos_visitante': [1, 3, 3, 1, 0, 3, 1, 3, 0, 3],
}

# Crear un DataFrame de pandas
df = pd.DataFrame(data)

# Crear una nueva columna "resultado" (1 si el local gana, 0 si empatan, -1 si el visitante gana)
df['resultado'] = np.where(df['goles_local'] > df['goles_visitante'], 1, 
                           np.where(df['goles_local'] < df['goles_visitante'], -1, 0))

# Features (X): Puntos del equipo local y visitante
X = df[['puntos_local', 'puntos_visitante']]

# Target (y): El resultado del partido
y = df['resultado']

# Dividir los datos en conjunto de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Crear el modelo de regresión logística
model = LogisticRegression()

# Entrenar el modelo
model.fit(X_train, y_train)

# Hacer predicciones sobre el conjunto de prueba
y_pred = model.predict(X_test)

# Evaluar el modelo
print(f"Precisión del modelo: {accuracy_score(y_test, y_pred)}")
print("Matriz de confusión:")
print(confusion_matrix(y_test, y_pred))

# Graficar los resultados
fig, ax = plt.subplots()
ax.scatter(X_test['puntos_local'], X_test['puntos_visitante'], c=y_pred, cmap='coolwarm', s=100, edgecolors='k', alpha=0.7)
ax.set_xlabel('Puntos del equipo local')
ax.set_ylabel('Puntos del equipo visitante')
ax.set_title('Pronóstico de resultados de la quiniela')
plt.show()
