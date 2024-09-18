import time
def ejercico1():
    palabra = str(input("Por favor ingresar palabra:"))
    Cantidad = int(input("por favor ingresar la cantidad de veces:"))
    for i in range(Cantidad):
        print("valor de la variable: ", i + 1)
        print(palabra)
        time.sleep(2)
#ejercico1()

def cantidad_años():
    Edad = int(input("ingrese la cantidad de años que tienes:"))
    for i in range(Edad):
        print("valor de la edad: ", i + 1)
        time.sleep(1)

#cantidad_años()

def calcular_edad():
    año = int(input("ingresar el año actual: "))
    añon = int(input("ingresar el año de nacimiento:"))
    edad = año- añon
    for i in range(edad + 1):
        print("Año: ",añon + i +1)
        print(i+1)
        time.sleep(1)
    return edad

#calcular_edad()

def numeros_impares():
    numero = int(input("ingrese el numero:"))

    for i in range(1, numero + 1, 1):
        print(i, end = ", \n ")
        time.sleep(1)
        if i == 60:
            break

#numeros_impares()

def reloj():
    tiempo = int(input("ingresa los segundos que deceas contar:"))
    
    for i in range(1, tiempo + 1, 1):
        print(i,"S", end = " \n")
        #time.sleep(1)
        if i == tiempo: 
            print("\33[101m"+"tiempo terminado"+"\33[0m")
            break;
        if i == 60:
            break
        
#reloj()

def interes_anual():
    cantidadDinero = int(input("cantidad de dinero al año: "))
    impuesto = float(input("cantidad de impuesto: "))
    cantidad_años= int(input("cantidad de años: "))
    for i in range (1,cantidad_años+1):
        print("Año: ", i)
        interes = cantidadDinero * (impuesto/100)
        cantidadDinero = cantidadDinero + interes
        print("Dinero al final del año: ", cantidadDinero)
        time.sleep(1)
interes_anual()