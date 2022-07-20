# crear un programa que le pida al usuario un numero natural y
# este muestre la tabla de multiplicar del numero ingrsado multiplicado desde el 1 hasta el 10
numero=int(input("ingrese un numero natural:"))
n2=int(input("ingrese el limete de la multiplicacion:"))
    # con n2 
LIMITE = n2
    # Comenzar en 1
contador = 1
while contador <= LIMITE:
        resultado = contador * numero
        print("{} x {} = {}".format(numero, contador, resultado))
      #el contado es como el fin del siclo para no creeas un bluque 
        contador = contador + 1

