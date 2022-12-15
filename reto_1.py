"""
Escribe una función que reciba dos palabras (String) y retorne
verdadero o falso (Bool) según sean o no anagramas.
- Un Anagrama consiste en formar una palabra reordenando TODAS
   las letras de otra palabra inicial.
- NO hace falta comprobar que ambas palabras existan.
- Dos palabras exactamente iguales no son anagrama.
"""


def main() -> None:
    print(is_anagram("Dualipa", "aauDlip")) # True
    print(is_anagram("Shark", "Shark")) # False
    print(is_anagram("dab", "Bad")) # True
    print(is_anagram("sorry", "rryoS")) # True
    print(is_anagram("NU", "uN")) # True
    print(is_anagram("Dualipa", "aauDl")) # False
    print(is_anagram("VOLOMOT", "MOtOloV")) # True
    print(is_anagram("ab", "ba")) # True
    print(is_anagram("1202", "2210")) # True


def is_anagram(word1: str, word2: str) -> bool:
    """
        Function that determines if two words are anagrams
        This function will return False if two words are identical
        Params
            word1[str] -> The first word to be evaluated
            word2[str] -> Second word to be compared

        Return
            bool -> True if the anagram between the two words exists, False otherwise
    """
    word1, word2 = word1.lower(), word2.lower()

    # Check if the words are strings
    if not word1.isalnum() or not word2.isalnum():
        return False

    return False if word1 == word2 else set(word1) == set(word2)


if __name__ == '__main__':
    main()