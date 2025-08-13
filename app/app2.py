from flask import Flask, render_template
import pandas_datareader.data as web
import datetime
import plotly.graph_objects as go
import plotly.io as pio


def obtener_datos_indra():
    print("Obteniendo datos de INDRA usando pandas_datareader...")
    start = datetime.datetime.now() - datetime.timedelta(days=365)
    end = datetime.datetime.now()
    try:
        data = web.DataReader('IDR.MC', 'yahoo', start, end)
        if data is not None and not data.empty:
            print("Datos de INDRA obtenidos exitosamente.")
        else:
            print("No se obtuvieron datos para INDRA.")
            data = None
    except Exception as e:
        print(f"Error al obtener los datos de INDRA: {e}")
        data = None


def generar_grafico(data):
    print("Generando gráfico...")
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=data.index, y=data['Close'], mode='lines', name='INDRA'))
    
    # Obtener y añadir datos de Telefónica
    print("Obteniendo datos de Telefónica...")
    data_telefonica = obtener_datos_telefonica()
    if data_telefonica is not None:
        fig.add_trace(go.Scatter(x=data_telefonica.index, y=data_telefonica['Close'], mode='lines', name='Telefónica', line=dict(color='red')))
    
    # Obtener y añadir datos de Mercedes-Benz
    print("Obteniendo datos de Mercedes-Benz...")
    data_mercedes = obtener_datos_mercedes()
    if data_mercedes is not None:
        fig.add_trace(go.Scatter(x=data_mercedes.index, y=data_mercedes['Close'], mode='lines', name='Mercedes-Benz', line=dict(color='black')))
    
    # Obtener y añadir datos de BBVA
    print("Obteniendo datos de BBVA...")
    data_bbva = obtener_datos_bbva()
    if data_bbva is not None:
        fig.add_trace(go.Scatter(x=data_bbva.index, y=data_bbva['Close'], mode='lines', name='BBVA', line=dict(color='blue')))
    
    fig.update_layout(title='Cotización de Acciones', xaxis_title='Fecha', yaxis_title='Precio de Cierre')
    print("Gráfico generado.")
    return pio.to_html(fig, full_html=False)
def obtener_datos_telefonica():
    print("Obteniendo datos de Telefónica usando pandas_datareader...")
    start = datetime.datetime.now() - datetime.timedelta(days=365)
    end = datetime.datetime.now()
    try:
        data = web.DataReader('TEF.MC', 'yahoo', start, end)
        print("Datos de Telefónica obtenidos exitosamente.")
    except Exception as e:
        print(f"Error al obtener los datos de Telefónica: {e}")
        data = None
    return data

def obtener_datos_mercedes():
    print("Obteniendo datos de Mercedes-Benz usando pandas_datareader...")
    start = datetime.datetime.now() - datetime.timedelta(days=365)
    end = datetime.datetime.now()
    try:
        data = web.DataReader('MBG.DE', 'yahoo', start, end)
        print("Datos de Mercedes-Benz obtenidos exitosamente.")
    except Exception as e:
        print(f"Error al obtener los datos de Mercedes-Benz: {e}")
        data = None
    return data

def obtener_datos_bbva():
    print("Obteniendo datos de BBVA usando pandas_datareader...")
    start = datetime.datetime.now() - datetime.timedelta(days=365)
    end = datetime.datetime.now()
    try:
        data = web.DataReader('BBVA.MC', 'yahoo', start, end)
        print("Datos de BBVA obtenidos exitosamente.")
    except Exception as e:
        print(f"Error al obtener los datos de BBVA: {e}")
        data = None
    return data
app = Flask(__name__)

@app.route('/')
def index():
    print("Cargando página principal...")
    data = obtener_datos_indra()
    if data is not None:
        grafico_html = generar_grafico(data)
        precio_actual = data['Close'][-1]
        tabla_html = data.to_html(classes='table table-striped', border=0)
        return render_template('index.html', grafico_html=grafico_html, precio_actual=precio_actual, tabla_html=tabla_html)
    else:
        return "Error al obtener datos."

if __name__ == '__main__':
    print("Iniciando la aplicación Flask...")
    app.run(debug=True)