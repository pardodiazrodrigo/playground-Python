import time
import sys


sys.setrecursionlimit(2000)
print(sys.getrecursionlimit())

def factorial(n):
    return 1 if n == 0 else n * factorial(n-1)

def factorial_iterativa(n):
    resultado = 1
    for i in range(n):
        resultado *= n-1
    return resultado

t0 = time.time()
a = factorial(1940)
t1 = time.time()
print(t1-t0)
t0 = time.time()
a = factorial_iterativa(1940)
t1 = time.time()
print(t1-t0)
