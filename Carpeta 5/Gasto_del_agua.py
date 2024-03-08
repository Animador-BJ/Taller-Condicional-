# Programa para calcular el gasto de agua de una vivienda

# Input
Gam2 = int(input("Ingrese la cantidad de m2 de agua gastados: "))

# Cuota fija mensual
cuota_fija = 10000

# Processing
if Gam2 <= 50:
    costo_agua = cuota_fija 
elif Gam2 <= 200:
    costo_agua = (Gam2 - 50) * 2000 + cuota_fija
else:
    costo_agua = (Gam2 - 200) * 3000 + 150000 

# Output
print(f"El gasto de agua para {Gam2} m2 es: ${costo_agua}")