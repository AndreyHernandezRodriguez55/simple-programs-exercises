#Escriba un programa que reciba como entrada el radio de un círculo y entregue como salida su perímetro y su área:
#Ingrese el radio: 5
#Perimetro: 31.4
#Área: 78.5
import math

radio = int(input("Escribe el radio de tu círculo: "))

area = math.pi * (radio ** 2)
perimetro = 2 * math.pi * radio

print(f"""De acuerdo al radio, tu área es: {area} y tu perímetro es: {perimetro}""")
