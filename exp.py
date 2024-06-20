# try:
#   ...
# except Exception
#   ...

class FileContentError(Exception):
    pass


def get_data():
    with open("number.txt") as f:
        v = f.read().strip()
        if not v:
            raise FileContentError
    return v


try:
    # val = int(input("Podaj liczbe: "))
    val = int(get_data())
    print(f"Wynik 1/{val}: {1/val}")
except ValueError:
    print("Wystapil blad: podaj dobra liczbe jako wejscie")
except ZeroDivisionError:
    print("Nie mozna dzielic przez 0, podaj inna liczba")
except FileContentError:
    print("Blad w zawartosci pliku")

try:
    {}.atrybut
except Exception as e:
    pass
