# exam 3
# X             10
# L             50
# C             100
# D             500
# M             1000

# Par exemple,  2s'écrit comme II en chiffres romains, seulement deux uns additionnés. 12 s'écrit  XII, ce qui est simplement X + II.
# Le nombre 27 s'écrit XXVII, ce qui est XX + V + II.


# Les chiffres romains sont généralement écrits du plus grand au plus petit, de gauche à droite. 
# Cependant, le chiffre quatre n’est pas IIII. Au lieu de cela, le chiffre quatre s’écrit IV. 
# Parce que le un est avant les cinq, nous le soustrayons, ce qui fait quatre. 
# Le même principe s’applique au nombre neuf, qui s’écrit IX. 

# Il existe six cas où la soustraction est utilisée :

# I peut être placé avant V(5) et X(10) pour faire 4 et 9. 
# X peut être placé avant L(50) et C(100) pour faire 40 et 90. 
# C peut être placé avant D(500) et M(1000) pour faire 400 et 900.



# Étant donné un chiffre romain, convertissez-le en nombre entier

# Exemple 1:

# Entrée : s = "III"
# Sortie : 3
# Explication : III = 3.


# Exemple 2 :

# Entrée : s = "LVIII"
# Sortie : 58
# Explication : L = 50, V= 5, III = 3.


# Exemple 3 :

# Entrée : s = « MCMXCIV »
# Sortie : 1994
# Explication : M = 1000, CM = 900, XC = 90 et IV = 4.

class Solution:
    """conversion de chiffres romains en entiers"""

    _VALUES = {
        "I": 1, "V": 5, "X": 10, "L": 50,
        "C": 100, "D": 500, "M": 1000,
    }

    @staticmethod
    def roman_to_int(s: str) -> int:
        """ Convertit un chiffre romain en entier."""
        total = 0
        prev = 0
        for ch in reversed(s):
            val = Solution._VALUES.get(ch, 0)
            if val < prev:
                total -= val
            else:
                total += val
            prev = val
        return total

# compatibility wrapper (optional)
def roman_to_int(s: str) -> int:
    return Solution.roman_to_int(s)

# tests rapides
if __name__ == "__main__":
    print(roman_to_int("III"))      # 3
    print(roman_to_int("LVIII"))    # 58
    print(roman_to_int("MCMXCIV"))  # 1994