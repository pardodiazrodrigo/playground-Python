def binarySearch(l1, x, verbose = False):
    '''Búsqueda binaria
    Precondición: la lista está ordenada
    Devuelve -1 si x no está en lista;
    Devuelve p tal que lista[p] == x, si x está en lista
    '''
    if verbose:
        print(f'[DEBUG] izq |der |medio')
    pos = -1 # Inicializo respuesta, el valor no fue encontrado
    izq = 0
    der = len(l1) - 1
    while izq <= der:
        medio = (izq + der) // 2
        if verbose:
            print(f'[DEBUG] {izq:3d} |{der:>3d} |{medio:3d}')
        if l1[medio] == x:
            pos = medio     # elemento encontrado!
        if l1[medio] > x:
            der = medio - 1 # descarto mitad derecha
        else:               # if l1[medio] < x:
            izq = medio + 1 # descarto mitad izquierda
    return pos


def whereInsert(l1,x,verbose=False):
    if verbose:
        print(f'[DEBUG] izq |der |medio')
    pos = -1
    left = 0
    right = len(l1)-1
    while left <= right:
        middle = (left + right) // 2
        if verbose:
            print(f'[DEBUG] {left:3d} |{right:>3d} |{middle:3d}')
        if left > x:
            return left
        if x > right:
            return right
        if middle < x:
            left = middle
        if middle > x:
            right = middle



a = [0,2,4,6]

if binarySearch(a,3,True) == -1:
    print(whereInsert(a,7,True))





