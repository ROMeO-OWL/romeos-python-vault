#23/09/23
while(True):
    c=int(input("Ingrese el password: "))
    if c == 2026:
        print("Welcome Player!!!")
        name = input("Ingrese su nombre: ")
        print("Hello "+name )
        edad = int(input("por favor ingrese edad para que ingrese a esta pagina web: "))
        if 0<edad<=101:
            print("Esta edad es valida\n")
            print("Eres mayor de edad" if edad>=18 else "Eres menor de edad")
        else:
           print("Edad no valida ")
        break
    else:
         print("Errorr!")
