# El siguiente programa muestra una peculiaridad del la
#   Conjetura de Collatz, o conjetura 3x+1. Dada una secuencia
#   de dónde sólo se toman los números impares de la lista superiores a 1,
#   el impar_i puede predecir si el impar_i+1 va sa ser mayor
#   o menor que él mismo.

def collatz(n):
    '''
    Devuelve el próximo número impar en la secuencia.

    Args:
        n (int): Entero positivo mayor que 0

    Raises:
        TypeError: n no es del tipo entero
        ValueError: n es menor a 1

    Returns:
        número: Próximo entero impar de la secuencia
    
    '''

    if type(n) is not int:
        raise TypeError("El argumento pasado debe ser un entero.")

    if n<1:
        raise ValueError("El argumento pasado debe ser mayor a 0.")

    if n&1:            # solo en caso de impares
        n = (n+1) + (n<<1)  # 3n+1
    while(not n&1):     # en culquier caso, mientras sea par
        n >>= 1             # n//2
    return n

def predecir_siguiente(n):
    '''
    Predice si el próximo entero impar en la secuencia de collatz será mayor o menor.
    Este resultado se obtiene dividiendo el número actual n entre 2 mediante una división entera. Si el
        cuociente obtenido es impar el siguiente número impar de la secuencia de collatz será mayor, en cambio
        si el cuociente obtenido es par el siguiente número impar de la secuencia de collatz será menor.
    Args:
        n (int): Entero positivo mayor que 1

    Raises:
        TypeError: n no es del tipo entero
        ValueError: n no es un valor impar mayor que 1

    Returns:
        boolean: True si el próximo impar será mayor, False si será menor
    
    '''

    if (not type(n) is int):
        raise TypeError("El argumento pasado debe ser un entero.")

    if n<2 or not n&1:
        raise ValueError("El argumento pasado debe ser un impar positivo mayor que 1.")

    # n&2 engloba las operaciones dividir por dos y comprobar si el número es impar:
    #    n = n>>1  o  n = n/2
    #    return n&1   o lo que es lo mismo: devuelve true si n&1 es 1 (n es impar) o false si n&1 es 0 (n es impar)
    return bool(n&2)      # True si n//2 es impar, False si es par


# Programa de demostración de uso
if __name__ == '__main__':
    
    for x in range(1, 101):
        print(f'collatz de {x}:')
        k = collatz(x)
        while(k != 1):
            print('{:>16}'.format(k), end=' ')
            print('sig. mayor' if predecir_siguiente(k) else 'sig. menor')
            k = collatz(k)
        print("{:>16} =\n".format(1))
