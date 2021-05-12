"""
@3N1CM4 ~ github.com/linusmaastok
2021-05-12
Subido DESPUES de entregada la tarea
>> Ayuda para los alumnos tutorados 2021
"""

# función que lee y valida que el número ingresado por teclado sea mayor al especificado en el código
# no recibe nada ingresado por el usuario, y retorna un numero entero válido
def validar(num):
    n = int(input())
    while n < num: n = int(input())
    return n

# función que voltea un numero entero
# recibe un numero entero y retorna el mismo numero volteado. EJ: 1234 -> 4321 ; 81113 -> 31118
def vol(num):
    inv = 0
    l = largo(num)
    while num > 0:
        inv = inv + num%10 * (10**(l-1))
        num = num // 10
        l = l - 1
    return inv 

# función que calcula el largo de un número entero
# recibe un número entero y devuelve el largo del numero. EJ: 1234 -> 4 ; 9 -> 1
def largo(num):
    largo = 0
    while num >= 1 :
        largo += 1
        num = num // 10
    return(largo)

# función que indica si un número es primo o no
# recibe un número entero y retorna True o False (Verdadero o Falso) si el número es primo.
# un número es primo si es mayor que 1 y es divisible entero solo de 1 y si mismo.
# EJ: 33 -> False ; 442109 -> True
def primo(num):
    if num == 0 or num == 1: return False
    for n in range(2, num):
        if num % n == 0:
            return False
    return True

# función que indica si un número es digit primo
# recibe un numero entero y devuelve True o False (Verdadero o Falso) si el numero es digitprimo.
# un número es digit primo cuando 2 o mas de sus dígitos son primos
# EJ: 133 -> True ; 444442689 -> False
def esDigitPrimo(n):
    l = largo(n)
    contador = 0
    for i in range(0,l):
        if primo(n%10) : contador = contador + 1
        n = n // 10
    if contador > 1 : return True
    else: return False

# función que indica la cantidad de dígitos primos que tiene un número.
# recibe un número entero y devuelve la cantidad de dígitos primos.
# EJ: 133389 -> 3 ; 100000000286999 -> 1
def cantprimo(n):
    l = largo(n)
    contador = 0
    for i in range(0,l):
        if primo(n%10) : contador = contador + 1
        n = n // 10
    return(contador)

# función que indica si un número es egotista o no.
# recibe un número entero y devuelve True o False (Verdadero o Falso).
# un número es egotista si la suma de cada uno de sus dígitos elevados al largo del número inicial es igual al número inicial.
# EJ: 1234 (1^4 + 2^4 + 3^4 + 4^4 != 1234) -> False ; 370 (3^3 + 7^3 + 0^3 = 370) -> True
def Egotista(num):
    num2 = num
    contador = 0
    while num >= 1:
        contador = contador + (num%10)**(largo(num2))
        num = num//10
    if contador == num2: return True
    else: return False

# función que entrega de manera gráfica, con el formato pedido en la tarea, si un número es egotista, digit-primo o egoprimo (egotista + digit-primo)
# recibe un número entero e imprime la solución en el formato solicitado
def analizar(n):
    ni = vol(n)
    n2 = ni
    contador = 0
    for i in range(0,largo(n)):
        dig = ni%10
        contador = contador + (dig ** largo(n))
        if largo(ni) > 1: print("{} ^ {} + ".format(dig,largo(n)), end= '')
        else: print("{} ^ {} = ".format(dig,largo(n)), end= '')
        ni = ni // 10
    
    if Egotista(n) : print("{} --> por lo tanto {} es egotista.".format(contador, n))
    else: print("{} --> por lo tanto {} NO es egotista.".format(contador, n))

    if cantprimo(n) == 0:
        print("{} NO tiene dígitos primos --> por lo tanto NO es digiprimo".format(n))
    elif cantprimo(n) == 1:
        print("Dígito(s) primo(s) de {} = ".format(n), end= '')
        for i in range(0,largo(n)):
            dig = n2%10
            if primo(dig) and dig != 0: print("{} --> por lo tanto NO es digit primo.".format(dig))
            n2 = n2 // 10
    else :
        aux = cantprimo(n)
        print("Dígito(s) primo(s) de {} = ".format(n), end= '')
        for i in range(0,largo(n)):
            dig = n2%10
            if primo(dig) and dig != 0:
                if aux > 1: 
                    print("{} , ".format(dig), end= '')
                else: print("{} --> por lo tanto es digit primo.".format(dig))
                aux = aux - 1
            n2 = n2 // 10

    if Egotista(n) and esDigitPrimo(n): print("En consecuencia el {} es ego primo.".format(n))
    else: print("En consecuencia el {} NO es ego primo.".format(n))

while True:
    n = validar(0)
    if n == 0: break
    analizar(n)
