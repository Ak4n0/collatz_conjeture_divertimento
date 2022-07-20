# collatz_conjeture_divertimento
Muestra una propiedad interesante del juego de Collatz

La encontré un día jugando con la conjetura de Collatz. Desconozco si ya se ha descubierto; los matemáticos son buenos, supongo que sí, pero no he encontrado documentación al respecto.

Trata de que dada una secuencia de la conjetura de Collatz, un número impar diferente de 1 indica, intrínsecamente, si el siguiente número impar de la secuencia será mayor o menor a este.

La operación matemática para conseguir esto es hacer una división entera entre dos. Si el cociente resultante es impar el próximo número impar de la lista será mayor, en cambio si el cociente resultante es par el próximo número impar de la lista será menor.

Por ejemplo tomemos el número 9 como ejemplo y solo los números impares de la lista de Collatz (recordar que la división es entera):

9  ->  9/2 = 4. 4 es par, el próximo número impar será menor.

7  ->  7/2 = 3. 3 es impar, el próximo número impar será mayor.

11 -> 11/2 = 5. 5 es impar, el próximo número impar será mayor.

17 -> 17/2 = 8. 8 es par, el próximo número impar será menor.

13 -> 13/2 = 6. 6 es par, el próximo número impar será menor.

5  ->  5/2 = 2. 2 es par, el próximo número impar será menor.

1  -> Se llegó al final.
