#14/10/23 by Romeo Lancelot:
from math import*
from colorama import*
#Funcion de triangulo rectangulo para allar CA,CO and Hip:
init()
def Rectangulo(n):
    while(n>0):
        r = int(input(Fore.CYAN+"Menu: \n1)Hipotenusa \n2)Cateto Ayacente \n3)Cateto Opuesto \n"))
        if (r==1):
            a=int(input("Ingrese cateto ayecente: "))
            o=int(input("Ingrese cateto opuesto: "))
            h=sqrt((a**2)+(o**2))
            print(f"El valor de la hipotenusa es {h}")
            break
        elif (r==2):
            h=int(input("Ingrese hipotenusa: "))
            o=int(input("Ingrese cateto opuesto: "))
            a=sqrt((h**2)-(o**2))
            print(f"El valor de la cateto ayacente es {a}")
            break
        elif (r==3):
            h=int(input("Ingrese hipotenusa: "))
            a=int(input("Ingrese cateto ayacente: "))
            o=sqrt((h**2)-(a**2))
            print(f"El valor de la cateto opuesto es {o}")
            break
        else:
            print("El numero que ingreso no es valido en el menu por favor intetelo de nuevo!!")
    return n

def main():
    print(Fore.CYAN+"Welcome\n")
    while True:
        menu  = input("Presione Y/y para ingresar, caso contrario N/n\n--> ").lower()
        if menu == 'y':menu=Rectangulo(1);break
        elif 'n'!= menu != 'y':print("Intentalo de nuevo\n")
        else:print("Adios!");break

if __name__ == '__main__':main()



