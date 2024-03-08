40# Programa que indica el IMC y su clasificación

# Input
Peso = int(input("Ingrese su peso actual: "))
Estatura = float(input("Ingrese su estatura actual: "))

# Processing
IMC = Peso / Estatura**2

if IMC < 16:
    Resultado = "Criterio de ingreso en hospital"
elif IMC <= 17:
    Resultado = "Infrapeso"
elif IMC <= 18.5:
    Resultado = "Bajo peso"
elif IMC <= 25:
    Resultado = "Peso normal (Saludable)"
elif IMC <= 30:
    Resultado = "Sobrepeso (Obesidad de grado 1)"
elif IMC <= 35:
    Resultado = "Sobrepeso crónico (Obesidad de grado 2)"
elif IMC <= 40:
    Resultado = "Obesidad premórbida (Obesidad de grado 3)"
elif IMC > 40:
    Resultado = "Obesidad mórbida (Obesidad de grado 4)"

# Output
print(f"Su IMC es {IMC:.2f} y sus resultados son: {Resultado}")