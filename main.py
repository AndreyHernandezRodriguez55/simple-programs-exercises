#Un alumno desea saber que nota necesita en el tercer certamen para aprobar un ramo.

#El promedio del ramo se calcula con la siguiente formula.

#NC=(C1+C2+C3)3
#NF=NC⋅0.7+NL⋅0.3
#Donde NC
#es el promedio de certámenes, NL
#el promedio de laboratorio y NF
#la nota final.

#Escriba un programa que pregunte al usuario las notas de los dos primeros certamen y la nota de laboratorio, y muestre la nota que necesita el alumno para aprobar el ramo con nota final 60.

#Ingrese nota certamen 1: 45
#Ingrese nota certamen 2: 55
#Ingrese nota laboratorio: 65
#Necesita nota 72 en el certamen 3

C1 = float(input("Enter grade for exam 1: "))
C2 = float(input("Enter grade for exam 2: "))
NL = float(input("Enter lab grade: "))


NF_needed = 60
NC_necesario = (NF_needed - (NL * 0.3)) / 0.7

C3_necesario = NC_necesario * 3 - C1 - C2
print(f"Necesita nota {C3_necesario:.2f} en el certamen 3")