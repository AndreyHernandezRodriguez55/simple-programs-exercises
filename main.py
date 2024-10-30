#Ejercicio sacado de [Lang09].

#Cuando un huevo es hervido en agua, las proteínas comienzan a coagularse cuando la temperatura sobrepasa un punto crítico. A medida que la temperatura aumenta, las reacciones se aceleran.

#En la clara, las proteínas comienzan a coagularse para temperaturas sobre 63°C, mientras que en la yema lo hacen para temperaturas sobre 70°C. Para hacer un huevo a la copa, la clara debe haber sido calentada lo suficiente para coagularse a más de 63°C, pero la yema no debe sobrepasar los 70°C para evitar obtener un huevo duro.

#El tiempo en segundos que toma al centro de la yema alcanzar Ty
 #°C está dado por la fórmula:

#t=M2/3cρ1/3Kπ2(4π/3)2/3ln[0.76To−TwTy−Tw],
#donde M
 #es la masa del huevo, ρ
 #su densidad, c
 #su capacidad calorífica específica y K
 #su conductividad térmica. Algunos valores típicos son:

#M=47[g]
 #para un huevo pequeño y M=67[g]
 #para uno grande,
#ρ=1.038[gcm−3]
#,
#c=3.7[Jg−1K−1]
#, y
#K=5.4⋅10−3[Wcm−1K−1
#].
#Tw
# es la temperatura de ebullición del agua y To
#la temperatura original del huevo antes de meterlo al agua, ambos en grados Celsius.

#Escriba un programa que reciba como entrada la temperatura original del huevo y muestre como salida el tiempo en segundos que le toma alcanzar la temperatura máxima para prepararlo a la copa.

#[Lang09]	Hans Petter Langtangen. A Primer on Scientific Programming with Python. Springer-Verlag, 2009.

M = 47  # Mass in grams for a large egg
rho = 1.038  # density g/cm^3
c = 3.7  # Heat capacity in J/(g K)
K = 5.4e-3  # Thermal conductivity in W/(cm·K)
Tw = 100  # Boiling point of water in °C
Ty = 70  # Maximum yolk temperature in °C


def time_to_boil(To):
    numerator = (M**(2/3)) * c * (rho**(1/3)) * K * (3.141592653589793**2) * ((4 * 3.141592653589793 / 3)**(2/3))

    # log(a) - log(b) = log(a/b)
    term1 = 0.76 * To - Tw
    term2 = Ty - Tw
    log_term = term1 / term2

    # Calculamos el tiempo
    t = numerator * log_term
    return t

original_temperature = float(input("Enter the original temperature of the egg (°C): "))
time = time_to_boil(original_temperature)

print(f"The time required to reach the maximum temperature is:{time:.2f} seg")