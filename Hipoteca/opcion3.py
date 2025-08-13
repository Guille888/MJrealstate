# Datos de la hipoteca
importe_hipoteca = 180000  # Importe total de la hipoteca
capital_amortizado = 86904  # Capital amortizado hasta la fecha
plazo_meses_restante = 173  # Plazo restante en meses
tipo_interes_anual = 1.75  # Tipo de interés anual para la opción 3
producto_vinculado_inicial = 17  # Producto vinculado seguro de hogar en la opción 3 (17€/mes)
seguro_inicial = 18.5  # Pago inicial del seguro de hogar (18.5€/mes)
incremento_seguro = 0.03  # Incremento anual estimado del seguro de hogar (3%)
plazo_anos = plazo_meses_restante / 12  # Plazo restante en años

# Función para calcular la cuota mensual
def calcular_cuota_mensual(importe_prestamo, tipo_interes_anual, plazo_meses):
    tipo_interes_mensual = tipo_interes_anual / 12 / 100
    cuota_mensual = importe_prestamo * (tipo_interes_mensual * (1 + tipo_interes_mensual)**plazo_meses) / ((1 + tipo_interes_mensual)**plazo_meses - 1)
    return cuota_mensual

# Calcular el capital pendiente
capital_pendiente = importe_hipoteca - capital_amortizado

# Calcular la cuota mensual sobre el capital pendiente
cuota_mensual_hipoteca = calcular_cuota_mensual(capital_pendiente, tipo_interes_anual, plazo_meses_restante)

# Estimar el coste total en los próximos años con el aumento del seguro
coste_total = 0
coste_seguro_anual = seguro_inicial * 12  # Seguro anual inicial (primer año)

# Sumar el coste durante el primer año (sin contar el seguro)
coste_total += cuota_mensual_hipoteca * 12  # Cuota mensual * 12 meses (primer año)

# Añadir el coste del seguro del primer año
coste_total += coste_seguro_anual

# Para los años siguientes, aumentar el coste del seguro en un 3% cada año
for año in range(2, int(plazo_anos) + 1):
    # Aumentar el coste del seguro
    coste_seguro_anual *= (1 + incremento_seguro)
    # Añadir el coste de la cuota de la hipoteca y el seguro del año actual
    coste_total += cuota_mensual_hipoteca * 12
    coste_total += coste_seguro_anual

# Mostrar el coste total
print(f"El coste total de la Opción 3 con incremento del seguro de hogar es: {coste_total:.2f}€")
