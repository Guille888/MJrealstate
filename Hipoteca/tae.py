import numpy as np
from scipy.optimize import fsolve

# Datos de la hipoteca
TIN_annual = 2 / 100  # Tipo de interés nominal anual (1.5%)
TIN_monthly = TIN_annual / 12  # Tipo de interés nominal mensual

# Datos adicionales
cuota_hipoteca = 619.88  # Cuota mensual de la hipoteca
productos_vinculados = 0  # Suma de los productos vinculados (seguro vida + seguro hogar)
cuota_total = cuota_hipoteca + productos_vinculados  # Cuota mensual total

importe_hipoteca = 180000  # Importe total de la hipoteca
capital_amortizado = 86904  # Capital amortizado hasta la fecha
plazo_restante_meses = 173  # Número de meses restantes de amortización

# Función para calcular la TAE
def calcular_tae(r):
    """
    r: tasa de interés mensual (en forma decimal, por ejemplo 0.01 para 1%)
    Esta función calcula el valor neto presente de los pagos futuros
    y lo compara con el valor inicial de la hipoteca.
    """
    pagos_totales = np.array([cuota_total for _ in range(plazo_restante_meses)])  # Pagos mensuales futuros
    capital_inicial = importe_hipoteca - capital_amortizado  # Capital restante a financiar

    # Calculamos el valor presente de los pagos futuros usando la tasa de interés mensual
    valor_presente = np.sum(pagos_totales / (1 + r) ** np.arange(1, plazo_restante_meses + 1))

    # Restamos el capital inicial para ver si la diferencia es cercana a cero
    return valor_presente - capital_inicial

# Usamos fsolve para encontrar la tasa que hace que el valor presente de los pagos sea igual al capital pendiente
tasa_mensual = fsolve(calcular_tae, 0.01)[0]  # Aproximamos la tasa mensual con fsolve
tae_aproximada = (1 + tasa_mensual) ** 12 - 1  # Convertimos a TAE anual

# Mostrar la TAE en porcentaje
print(f"La TAE aproximada de tu hipoteca es: {tae_aproximada * 100:.2f}%")


