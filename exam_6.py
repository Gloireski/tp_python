# exam 6
import re
from typing import Tuple

def parse_temp(s: str) -> Tuple[float, str]:
    """Parse input like '45F', '102C', ' 32.5 f ' and return (value, unit)."""
    s = s.strip().upper() #Supprime les espaces et met tout en majuscules
    m = re.fullmatch(r'([+-]?\d+(?:\.\d+)?)\s*([CF])', s) #vérifie que toute la chaîne correspond
    #([+-]?\d+(?:\.\d+)?) capture la partie numérique (entier ou flottant)
    #\s* capture les espaces éventuels entre le nombre et l'unité
    #([CF]) capture l'unité (C ou F)
    if not m:
        raise ValueError("Format invalide — utilisez par exemple: 45F ou 102C")
    value = float(m.group(1))
    # group(1) recupere la partie numérique
    # group(2) recupere l'unité
    unit = m.group(2)
    return value, unit

def convert_and_print(s: str) -> None:
    try:
        value, unit = parse_temp(s)
    except ValueError as e:
        print(e)
        return

    if unit == "F":
        c = (value - 32.0) / 1.8
        print(f"La température en Celsius est de {c:.2f} °C.")
    else:  # unit == "C"
        f = value * 1.8 + 32.0
        print(f"La température en Fahrenheit est de {f:.2f} °F.")

if __name__ == "__main__":
    user = input("Input the temperature to convert (e.g., 45F, 102C): ")
    convert_and_print(user)