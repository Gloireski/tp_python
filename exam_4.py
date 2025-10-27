# ...existing code...
from typing import List

class Solution:
    """Incrémente un grand entier représenté par une liste de chiffres."""

    @staticmethod
    def plus_one(digits: List[int]) -> List[int]:
        """Ajoute 1 aux digits en place, retourne le résultat."""
        # validation (optionnelle)
        for d in digits:
            if not (0 <= d <= 9):
                raise ValueError("Chaque élément de digits doit être entre 0 et 9.")
        # parcourir de droite à gauche
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits  # pas de retenue restante
            digits[i] = 0  # retenue de 1
        # si tous les chiffres étaient 9
        return [1] + digits

# ...existing code...
if __name__ == "__main__":
    print(Solution.plus_one([1,2,3]))   # [1,2,4]
    print(Solution.plus_one([4,3,2,1])) # [4,3,2,2]
    print(Solution.plus_one([9]))       # [1,0]