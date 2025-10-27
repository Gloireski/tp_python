# exam 1
# Étant donné une chaîne s, renvoie la plus longue sous-chaîne palindromique dans s
# Exemple:
#  s = "babad" -> "bab" ou "aba"
#  s = "cbbd"  -> "bb"

class Solution:
    def longest_palindrome(self, s: str) -> str:
        n = len(s)
        if n == 0:
            return ""
        start, end = 0, 0

        def expand(left: int, right: int) -> int:
            while left >= 0 and right < n and s[left] == s[right]:
                left -= 1
                right += 1
            # La longueur du palindrome trouvé
            print(f"Debug: Found palindrome {s[left + 1:right]} from index {left + 1} to {right - 1}")
            return right - left - 1

        for i in range(n):
            len1 = expand(i, i) # palindrome impair
            len2 = expand(i, i + 1) # palindrome pair
            maxlen = max(len1, len2)
            if maxlen > end - start + 1:
                start = i - (maxlen - 1) // 2
                end = i + maxlen // 2
        return s[start:end + 1]


def longest_palindrome(s: str) -> str:
    return Solution().longest_palindrome(s)


if __name__ == "__main__":
    examples = ["babad", "cbbd", "", "a", "forgeeksskeegfor"]
    for ex in examples:
        print(f"{ex!r} -> {longest_palindrome(ex)!r}")