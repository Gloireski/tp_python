# exam 2
class Solution:
    """Container for solution methods."""

    @staticmethod
    def score_of_string(s: str) -> int:
        """Retourne la somme de la différence absolue entre les valeurs ASCII des caractères adjacents"""
        return sum(abs(ord(a) - ord(b)) for a, b in zip(s, s[1:]))

# compatibility wrapper
def score_of_string(s: str) -> int:
    return Solution.score_of_string(s)

# tests rapides
if __name__ == "__main__":
    print(score_of_string("hello"))  # 13
    print(score_of_string("zaz"))    # 50
    print(score_of_string(""))       # 0
    print(score_of_string("a"))      # 0
