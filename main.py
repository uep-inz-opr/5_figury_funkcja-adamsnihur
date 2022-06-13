from math import pi

lista = []
figura = []
ile_figur = int(float(input().strip()))

for i in range(ile_figur):
    lista.append(input().split())

def pole_kola(a):
        return pi * a * a
def pole_prostokata(a,b):
        return a * b
def pole_trojkata(a,b,c):
        return (x*(x-a)*(x-b)*(x-c)) ** 0.5

pole = 0

for figura in lista:

    if len(figura) == 1:
        a = float(figura[0])
        pole += pole_kola(a)

    elif len(figura) == 2:
        a = float(figura[0])
        b = float(figura[1])
        pole += pole_prostokata(a,b)

    elif len(figura) == 3:
        a = float(figura[0])
        b = float(figura[1])
        c = float(figura[2])
        x = ((a + b + c)/2)
        pole += pole_trojkata(a,b,c)

    else:        
        print("Błąd: można podać maksymalnie 3 liczby")
        break

print(round(pole,2))
