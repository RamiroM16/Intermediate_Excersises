### Challenges ###

"""
El fmaoso "FIZZ BUZZ"
Escribe un programa que muestre por consola (con un print) los
Numeros de 1 a 100 (Ambos incluidos y con un salto de linea entre
cada impresion), sustituyendo los siguientes:
Multiplos de 3 por la palabra "fizz"
Multiplos de 5 por la palabra "buzz"
Multiplos de 3 y de 5 a la vez por la palabra "fizzbuzz"
"""
def fizzbuzz0():
    i=1
    while i<=100:
        if i%3 == 0 and i%5 == 0:
            print("fizzbuzz")
        elif i%3 == 0:
            print("fizz")
        elif i%5 == 0:
            print("buzz")
        else:
            print(i)
        i += 1


def fizzbuzz():
    for i in range(1,101):
        if i%3 == 0 and i%5 == 0:
           print("fizzbuzz")
        elif i%3 == 0:
            print("fizz")
        elif i%5 == 0:
            print("buzz")
        else:
            print(i)

"""
Es un anagrama?
Escribe una funcion que reciba dos palabras (string) y retorne
verdadero o falso (Bool) segun sean o no anagramas.
- Un anagrama consiste en formar una palabra reordenando TODAS
  las letras de otra palabra inicial.
- No hace falta comprobar que ambas palabras existan.
- Dos palabras exactamente iguales no son anagrama.
"""

def anagrama():
    palabra1 = input("Escribe la primera palabra: ")
    palabra2 = input("Escribe la segunda palabra: ")
    if palabra1 == palabra2:
        return False
    return sorted(palabra1.lower()) == sorted(palabra2.lower())

#print(anagrama())

"""
Escribe un programa que imprima los 50 primeros numeros de la sucerion
de Fibonacci empezando en 0.
- La serie Fibonacci se compone por una sucesion de numeros en
  la que el siguiente siempre es la suma de los dos anteriores.
  0, 1, 1, 2, 3, 5, 8, 13...
"""

def fibonacci():
    i=1
    j=0
    for k in range(50):
        print(j)
        fib = i + j
        j = i
        i = fib
        

#fibonacci()

"""
Es un numero primo?
Escribe un programa que se encargue de comprobar si un numero es o no primo.
Hecho esto, imprime los numeros primos entre 1 y 1000
"""

def num_primo():
    for i in range(2,101):
        esprimo=True
        for j in range(2,i):
            if i%j ==0:
                esprimo=False
        if esprimo:
            print(i)
            
#num_primo()

"""
Crea un programa que invierta el orden de una cadena de texto
sin usar funciones propias del lenguaje que lo hagan de forma automatica
- Di le pasamos "Hola mundo" nos retornaria "odnum aloH"
"""

def string_inv():
    my_string = input("Escribe una cadena para invertir: ")
    txt_len= len(my_string)
    for i in range(txt_len):
        print(my_string[txt_len-i-1])

    


string_inv()