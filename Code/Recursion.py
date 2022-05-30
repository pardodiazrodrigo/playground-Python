import time

def factorial(n):
    return 1 if n == 0 else n * factorial(n-1)


def regresiva(n):
    print(n)
    time.sleep(1)
    print("0 \nFIN") if n == 1 else regresiva(n-1)

def potencia(n,m):
    return 1 if m == 0 else n * potencia(n,m-1)


def sumar(lista):
    return 0 if lista == [] else lista[0] + sumar(lista[1:])

a = [1,2,3,4,5,6,7,8,9]

def invertir(lista):
    return lista if lista == [] else [lista[-1]] + invertir(lista[:-1])

    # if lista == []:
    #     return lista
    # else:
    #     invertida  = [lista[-1]] + invertir(lista[:-1])
    #     return invertida

a = [1,[2,3],4]
def aplanar_lista(datos):
    plana = []
    for dato in datos:
        if type(dato) == int:
            plana.append(dato)
        elif type(dato) == list:
            for elemento in dato:
                plana.append(elemento)
    return plana

print(aplanar_lista(a))