# Input
a = int(input("Ingrese el primer digito de la suma: "))
b = int(input("Ingrese el segundo digito de la suma: "))
c = int(input("Ingrese el resultado que usted cree correcto: "))

# Procesamiento
if a + b == c:
    print(f"¡Correcto! La suma de los números {a} + {b} es igual a: {c}")
else:
    resultado_correcto = a + b
    print(f"Incorrecto. La suma de los números {a} + {b} no es igual a: {c}. La respuesta correcta es {resultado_correcto}.")
1
