#Escriba un programa que entregue la parte decimal de un número real ingresado por el usuario.

#Ingrese un numero: 4.5
#0.5
#Ingrese un numero: -1.19
#0.19


nomber= float(input("Enter a number: "))

decimal_part = abs(nomber) - abs(int(nomber))

print(decimal_part)