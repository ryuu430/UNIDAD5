from colorama import Fore, Style
try:
    num1 = float(input("Primer número: "))
    num2 = float(input("Segundo número: "))
    operacion = input("Operación (+, -, *, /): ")

    if operacion == '+':
        print(num1 + num2)
    elif operacion == '-':
        print(num1 - num2)
    elif operacion == '*':
        print(num1 * num2)
    elif operacion == '/':
        print(num1 / num2)
        
except ValueError:
    print(Fore.RED+"Error escrive numeros validos" +Style.RESET_ALL)
except ZeroDivisionError:
    print(Fore.RED+"No se puede dividir en 0" +Style.RESET_ALL)
