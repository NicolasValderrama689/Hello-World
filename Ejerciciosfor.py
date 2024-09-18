
import time
def ejercicio1 ():
    palabra= str(input("Por favor ingresar palabra:"))
    cantidad= str(input("Por favor imgresar cantidad de veces: "))
    for i in range(cantidad):
        print("valor de la variable i:",i+1)
        time.sleep(2)
        print(palabra)
    return palabra
#ejercicio1()

def ejercicio2():
    edad= int(input("Por favor ingresar los años:"))
    for i in range(edad):
        print("Edad i:",i+1)
        time.sleep(1)
        print(i+1)
    
ejercicio2()