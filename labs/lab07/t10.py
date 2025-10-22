def convertLeterToDec(letter: str) -> int:
    # "1" -> 1, "3" -> 3, "A" -> 10, "F" -> 15
    if letter.isdigit():
        return int(letter)

    if "A" <= letter <= "Z":
        return 10 + ord(letter) - ord("A")

    return 0

def convertDecToLetter(n: int) -> str:
    #   1 -> 1, 10 -> A, 15 -> F
    if n >= 36:
        return ""

    if 0 <= n <= 9:
        return str(n)
    else:
        return chr(ord("A") + n - 10)


print(convertLeterToDec("1"))
print(convertLeterToDec("5"))
print(convertLeterToDec("A"))
print(convertLeterToDec("F"))
print(convertLeterToDec("Z"))

print(convertDecToLetter(0))
print(convertDecToLetter(1))
print(convertDecToLetter(5))
print(convertDecToLetter(10))
print(convertDecToLetter(15))
print(convertDecToLetter(17))