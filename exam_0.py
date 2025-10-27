# exam 0

def length_of_last_word(s: str) -> int:
    """ renvoie la longueur du dernier mot de la chaîne (séparée par des espaces)"""
    s = s.rstrip()
    if not s:
        return 0
    last_space = s.rfind(' ')
    print(f"Debug: last_space index = {last_space}")
    print(f"Lenght of the string after rstrip: {len(s)}")
    return len(s) - last_space - 1

# Test rapides
if __name__ == "__main__":
    tests = [
        ("Hello World", 5),
        (" Envole-moi vers la lune ", 4),
        ("Luffy est toujours Joyboy", 6),
        ("", 0),
        ("   ", 0),
        ("single", 6),
    ]
    for inp, expect in tests:
        print(repr(inp), "->", length_of_last_word(inp), "expected", expect)
