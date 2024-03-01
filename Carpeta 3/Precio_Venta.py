# Programa que indica el precio de venta de un articulo dado

# imput
Precio_costo = int(input("lo que vale el articulo: "))

# processing

if Precio_costo < 3000:
    ganancia = Precio_costo * 0.15
    print(f"La ganancia es: {ganancia}")
    
elif Precio_costo < 6000:
     ganancia = 500
     print(f"La ganancia es: {ganancia}")
    
    
else:
    ganancia = Precio_costo * 0.25
    print(f"La ganancia es: {ganancia} ") 
    