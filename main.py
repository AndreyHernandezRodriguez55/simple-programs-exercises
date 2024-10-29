#Escriba un programa que reciba como entrada el radio de un círculo y entregue como salida su perímetro y su área:
#Ingrese el radio: 5
#Perimetro: 31.4
#Área: 78.5
import math
radio = int(input("Write the radius of your circle: "))
area = math.pi * (radio ** 2)
perimeter = 2 * math.pi * radio
print(f"""According to the radius, your area is: {area} and your perimeter is: {perimeter }""")