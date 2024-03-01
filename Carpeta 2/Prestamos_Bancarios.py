# Programa que permita realizar un préstamo bancario,

# input
print("---------------------------------------------")

sueldo = int(input("Digite la cantidad de sueldo que gana: "))

deudas = input("Diga si tiene o no tiene deudas: ")

if sueldo >= 945200:
    if deudas == "no":
        rta = "APROBADO"
    else:
        rta = "RECHAZADO"
else:
    rta = "RECHAZADO"

# output

print("---------------------------------------------")
print("Su Prestamoa sido " + rta )