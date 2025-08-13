from flask import Flask, render_template
import yfinance as yf
import plotly.graph_objs as go
import plotly.io as pio

from openai import OpenAI
from openai import AzureOpenAI
import configparser

# Leer el archivo de configuración
config = configparser.ConfigParser()
config.read('Credencial_IA.mbc')

# Obtener las variables del archivo de configuración
api_version = config.get('DEFAULT', 'api_version')
azure_endpoint = config.get('DEFAULT', 'azure_endpoint')
api_key = config.get('DEFAULT', 'api_key')
model_name = config.get('DEFAULT', 'model')

# Crear el cliente con las variables leídas
print("Creando cliente AzureOpenAI...")  # Seguimiento
client = AzureOpenAI(
    api_version=api_version,
    azure_endpoint=azure_endpoint,
    api_key=api_key
)

def estimar_valor_accion(accion):
    print(f"Estimando valor para {accion}...")  # Seguimiento
    messages = [
        {"role": "system", "content": "Eres un modelo de predicción financiera."},
        {"role": "user", "content": f"¿Cuál será el valor de la acción de {accion} en el próximo año?"}
    ]

    response = client.chat.completions.create(
        model=model_name,
        messages=messages,
        timeout=40,
        temperature=0.0
    )

    # Leer el archivo de configuración
    config.read('Credencial_IA.mbc')
    print("Archivo de configuración leído.")  # Seguimiento

    # Obtener las variables del archivo de configuración
    try:
        api_version = config.get('DEFAULT', 'api_version')
        azure_endpoint = config.get('DEFAULT', 'azure_endpoint')
        api_key = config.get('DEFAULT', 'api_key')
        model_name = config.get('DEFAULT', 'model')
        print("Variables de configuración obtenidas correctamente.")  # Seguimiento
    except configparser.NoOptionError as e:
        print(f"Error en la configuración: {e}")  # Seguimiento de errores

        assistant_message = response.choices[0].message.content
        print(f"Estimación para {accion}: {assistant_message}")  # Seguimiento
        return assistant_message

# Definir la aplicación Flask
app = Flask(__name__)
print("Aplicación Flask inicializada.")

def generar_grafico(data):
    print("Generando gráfico...")  # Añadido para verificar el inicio de la generación del gráfico
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=data.index, y=data['Close'], mode='lines', name='INDRA'))
    print("Obteniendo datos de Telefónica...")  # Seguimiento
    telefonica = yf.Ticker("TEF.MC")
    data_telefonica = telefonica.history(period="20y")
    print("Datos de Telefónica obtenidos.")  # Seguimiento
    fig.add_trace(go.Scatter(x=data_telefonica.index, y=data_telefonica['Close'], mode='lines', name='Telefónica', line=dict(color='red')))
    # Obtener y añadir datos de Mercedes-Benz
    print("Obteniendo datos de Mercedes-Benz...")  # Seguimiento
    mercedes = yf.Ticker("MBG.DE")
    data_mercedes = mercedes.history(period="20y")
    print("Datos de Mercedes-Benz obtenidos.")  # Seguimiento
    # Añadir datos de Mercedes-Benz
    fig.add_trace(go.Scatter(x=data_mercedes.index, y=data_mercedes['Close'], mode='lines', name='Mercedes-Benz', line=dict(color='black')))

    fig.update_layout(title='Cotización de INDRA en el último año', xaxis_title='Fecha', yaxis_title='Precio de Cierre')
    print("Gráfico generado.")  # Añadido para confirmar que el gráfico se ha generado
    return pio.to_html(fig, full_html=False)

def obtener_datos_indra():
    print("Obteniendo datos de INDRA...")
    indra = yf.Ticker("IDR.MC")
    data = indra.history(period="20y")
    print("Datos obtenidos.")
    return data

@app.route('/')
def index():
    print("Cargando página principal...")
    data = obtener_datos_indra()
    grafico_html = generar_grafico(data)
    precio_actual = data['Close'][-1]
    # Convertir los datos de cotización a HTML
    print("Convirtiendo datos de cotización a tabla HTML...")  # Seguimiento
    tabla_html = data.to_html(classes='table table-striped', border=0)
    print("Tabla HTML generada.")  # Seguimiento
    return render_template('index.html', grafico_html=grafico_html, precio_actual=precio_actual, tabla_html=tabla_html)


@app.route('/actualizar')
def actualizar():
    print("Actualizando datos y gráfico...")
    data = obtener_datos_indra()
    grafico_html = generar_grafico(data)
    precio_actual = data['Close'][-1]
        # Convertir los datos de cotización a HTML
    print("Convirtiendo datos de cotización a tabla HTML...")  # Seguimiento
    tabla_html = data.to_html(classes='table table-striped', border=0)
    print("Tabla HTML generada.")  # Seguimiento
    return render_template('index.html', grafico_html=grafico_html, precio_actual=precio_actual, tabla_html=tabla_html)

if __name__ == '__main__':
    print("Iniciando la aplicación Flask...")
    app.run(debug=True)