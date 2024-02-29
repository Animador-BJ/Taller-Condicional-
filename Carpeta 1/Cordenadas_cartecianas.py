# Programa saber la ubicacion de x & y en el plano carteciano

# input
print("---------------------------------------------")

x = int(input("Digite la posicion de x en el plano: "))
y = int(input("Digite la posicion de y en el plano: "))

# prosesing
if x == 0:
    if y == 0:
        print("La coordenada" ,(x , y), "esta en el origen")
    else:
        print("La coordenada" ,(x , y), "esta en el eje y")
elif y == 0:
    print("La coordenada" ,(x , y), "esta en el eje x")
elif x > 0:
    if y > 0:
        print("La coordenada" ,(x , y), "esta en el cuadrante 1")
    else: 
        print("La coordenada" ,(x , y), "esta en el cuadrante 4")
elif y < 0:
    print("La coordenada" ,(x , y), "esta en el cuadrante 3")
else: 
    print("La coordenada" ,(x , y), "esta en el cuadrante 2")
    

