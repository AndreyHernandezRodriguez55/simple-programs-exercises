#Escriba un programa que calcule el promedio de 4 notas ingresadas por el usuario:
#Primera nota: 55
#Segunda nota: 71
#Tercera nota: 46
#Cuarta nota: 87
#El promedio es: 64.75

note1 = float(input("enter your first note: "))
note2 = float(input("Enter your second note : "))
note3 = float(input("Enter your third note : "))
note4 = float(input("enter your fourth note: "))

average = (note1 + note2 + note3 + note4) / 4
print(f"the average is: {average:.2f}")