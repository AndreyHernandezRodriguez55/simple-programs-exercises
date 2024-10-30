#Escriba un programa que pregunte al usuario la hora actual t del reloj y un número entero de horas h, que indique qué hora marcará el reloj dentro de h horas:

#Hora actual: 3
#Cantidad de horas: 5
#En 5 horas, el reloj marcara las 8
#Hora actual: 11
#Cantidad de horas: 43
#En 43 horas, el reloj marcara las 6


current_time= int(input("current time: "))
hour_quantity= int(input("Chour quantity:  "))

new_time=(hour_quantity + current_time) %12

if new_time == 0:
    new_time= 12

    print(f"In {current_time} hours, the clock will read {new_time} ")
