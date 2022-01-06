import os
from time import sleep as sl
import random as rd

rojo = '\033[31m'
verde = '\033[32m'
amarillo = '\033[93m'
reinicio = '\033[0m'

ppt = ["Tijera", "Piedra", "Papel"]

#Funciones
def scl():
    sl(1)
    try:
        os.system("clear")
    except:
        os.system("cls")

def cc():
    cc = str(input("Otra Vez (Y/n): "))
    if cc == "Y" or cc == "y":
        game()
    elif cc == "N" or cc == "n":
        scl()
        print("{}Adios :(\n{}".format(rojo, reinicio))

def game():
    os.system("clear")
    print('''
         Kr4K1ng
"Piedra - Papel - Tijera"

[ 1 ] Tijera
[ 2 ] Papel
[ 3 ] Piedra

[ 0 ] Salir

    ''')
    a = int(input("Selecciona uno para jugar: "))

    #Opcion1
    if a == 1 and ppt[0]:
        b = rd.choice(ppt)
        print("\nTijera y", b)
        if b == "Piedra" and ppt[0]:
            print("{}\nPierdes\n{}".format(rojo, reinicio))
        elif b == "Tijera" and ppt[0]:
            print("{}\nEmpate\n{}".format(amarillo, reinicio))
        else:
            print("{}\nGanas\n{}".format(verde, reinicio))
        cc()
    #Opcion2
    elif a == 2 and ppt[2]:
        c = rd.choice(ppt)
        print("\nPapel y", c)
        if c == ppt[1]:
            print("{}\nGanas\n{}".format(verde, reinicio))
        elif c == ppt[2]:
            print("{}\nEmpate\n{}".format(amarillo, reinicio))
        else:
            print("{}\nPierdes\n{}".format(rojo, reinicio))
        cc()

    #Opcion3
    elif a == 3 and ppt[1]:
        d = rd.choice(ppt)
        print("\nPiedra y", d)
        if d == ppt[2]:
            print("{}\nPierdes\n{}".format(rojo, reinicio))
        elif d == ppt[0]:
            print("{}\nGanas\n{}".format(verde, reinicio))
        else:
            print("{}\nEmpate\n{}".format(amarillo, reinicio))
        cc()

    #Salir
    elif a == 0:
        scl()
        print("{}Adios :(\n{}".format(rojo, reinicio))

    #Error
    else:
        print("{}\nOpcion Incorrecta!\n{}".format(rojo, reinicio))
        scl()
        game()

#Ej
game()

#Fin