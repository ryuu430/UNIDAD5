from colorama import Fore, Style
# PROBLEMA: Simula un cajero donde el usuario tiene 100€
# Pregunta cuánto quiere retirar y actualiza el saldo
# No puede retirar más de lo que tiene, ni cantidades negativas, ni texto
try:
    saldo = 100
    print(f"Saldo actual: {saldo}€")
    
    # Con try-except:
    retiro = float(input("¿Cuánto quieres retirar? "))
    if retiro < 0:
        print("No puedes retirar cantidades negativas")
    
    # error de assert
    assert retiro > 0

    saldo -= retiro
    print(f"Retirado: {retiro}€")
    print(f"Nuevo saldo: {saldo}€")

except ValueError:
    print(Fore.RED+"ERROR: Escrive un numero valido"+Style.RESET_ALL)
except AssertionError:
    print(Fore.RED+"ERROR: Tiene que ser positivo"+Style.RESET_ALL)