# Programa que indica el precio de venta de un articulo dado

# Input
Precio_costo = int(input("Ingrese el costo del artículo: "))

# Processing
if Precio_costo < 3000:
    ganancia = Precio_costo * 0.15
    print(f"La ganancia es: {ganancia}")
    print(f"Precio_costo + {ganancia} = {Precio_costo + ganancia}")
    
elif Precio_costo < 6000:
    ganancia = 500
    print(f"La ganancia es: {ganancia}")
    print(f"Precio_costo + {ganancia} = {Precio_costo + ganancia}")
    
else:
    ganancia = Precio_costo * 0.25
    print(f"La ganancia es: {ganancia}")
    print(f"Precio_costo + {ganancia} = {Precio_costo + ganancia}")