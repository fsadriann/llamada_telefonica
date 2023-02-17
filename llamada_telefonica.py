#input

num_min = int(input("Digite el numero de minutos: "))

#processing

if num_min <4:
    y = 300
else:
    y = (num_min*50) + 300 - 150

if y > 999:
    msj = "mil"
else:
    msj = " pesos"

#output
print("El costo de la llamada es de " + str(y) + msj)