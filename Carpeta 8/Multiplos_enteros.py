# Input
a = int(input("Ingrese un número: "))
b = int(input(f"Ingrese un múltiplo del número {a}: "))

# Procesamiento y salida
if a % b == 0 or b % a == 0:
    print(f"Los números {a} y {b} son múltiplos")
else:
    multiplo_cercano = b - (b % a)
    print(f"Los números {a} y {b} no son múltiplos. El múltiplo más cercano a {b} y multiplo de {a} es {multiplo_cercano}")

