from colorama import Style, Fore
# PROBLEMA: Pide al usuario un índice y muestra el elemento en esa posición
try:
    amigos = ["Ana", "Luis", "Carlos", "María"]

    # Con try-except:
    indice = int(input(f"Elige un índice (0-{len(amigos)-1}): "))
    print(f"Tu amigo es: {amigos[indice]}")
except ValueError:
    print(Fore.RED+"ERROR: escrive un numero valido"+Style.RESET_ALL)
except IndexError:
    print(Fore.RED+"ERROR: escrive del 0 al 3"+Style.RESET_ALL)