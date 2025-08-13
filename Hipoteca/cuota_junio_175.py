# Función para calcular la cuota mensual
def calcular_cuota_mensual(importe_prestamo, tipo_interes_anual, plazo_meses):
    # Convertir el tipo de interés anual a mensual
    tipo_interes_mensual = tipo_interes_anual / 12 / 100
    
    # Calcular la cuota mensual usando la fórmula de amortización
    cuota_mensual = importe_prestamo * (tipo_interes_mensual * (1 + tipo_interes_mensual)**plazo_meses) / ((1 + tipo_interes_mensual)**plazo_meses - 1)
    
    return cuota_mensual

# Datos de la hipoteca
importe_hipoteca = 180000  # Importe total de la hipoteca
capital_amortizado = 86904  # Capital amortizado hasta la fecha
plazo_meses_restante = 173  # Plazo restante en meses

# Calcular el capital pendiente
capital_pendiente = importe_hipoteca - capital_amortizado

# Nuevo tipo de interés anual (1,75%)
tipo_interes_anual = 1.75  # Tipo de interés anual actualizado (en porcentaje)

# Calcular la cuota mensual sobre el capital pendiente con el nuevo tipo de interés
cuota = calcular_cuota_mensual(capital_pendiente, tipo_interes_anual, plazo_meses_restante)

# Mostrar el resultado
print(f"La nueva cuota mensual con un tipo de interés del 1,75% es: {cuota:.2f}€")
