# Programa para calcular el costo de agua por m3

# Input
Gasto_agua = int(input("Digite el gasto de agua en su vivienda (en m3): "))

# Cuota fija mensual
cuota_fija = 10000

# Variable para la cantidad de m³ que excede los primeros 50 m³ gratuitos
exceso_m3 = max(0, Gasto_agua - 50)

# Processing
if Gasto_agua <= 50:
    Pago = cuota_fija  # Los primeros 50 m³ son gratis
else:
    Pago = exceso_m3 * 2000 + cuota_fija

# Output 
print(f"El dinero a pagar por el gasto del agua es: {Pago}")
print(f"Cantidad de m³ que excede los primeros 50 m³: {exceso_m3}")