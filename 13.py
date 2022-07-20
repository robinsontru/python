contadorpares=int(0)
contadoresinpares=int(0)
numero=int(input("ingrese un numero:"))
while (numero!=0):
  if numero%2==0:
    contadorpares=contadorpares+1

  else:
    contadoresinpares=contadoresinpares+1
    numero=int(input("ingrese un numero"))
print("cantidad de numeros pares" , str(contadorpares),"cantidad de numeros pares", str(contadoresinpares))
