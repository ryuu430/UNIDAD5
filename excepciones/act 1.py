from colorama import Fore, Style
try:
    num1 = input("Escribe el primer número: ")
    num2 = input("Escribe el segundo número: ")
    resultado = int(num1) / int(num2)
    print(f"Resultado: {resultado}")

except ValueError:
    print(Fore.RED+"ERROR 1: Escrive un numero valido"+Style.RESET_ALL)
except ZeroDivisionError:
    print(Fore.RED+"ERROR 2: No se divide en 0"+Style.RESET_ALL)
