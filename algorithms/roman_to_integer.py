ROMAN_TO_INTEGER_MAP = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000,
}


def romanToInt(s):
    total = 0
    for index in range(len(s) - 1):
        roman_number = s[index]
        number = ROMAN_TO_INTEGER_MAP[roman_number]
        next_number = ROMAN_TO_INTEGER_MAP[s[index + 1]]
        shift = -1 if number < next_number else 1
        total += number * shift
    total += ROMAN_TO_INTEGER_MAP[s[-1]]
    return total


if __name__ == "__main__":
    assert romanToInt("I") == 1
    assert romanToInt("II") == 2
    assert romanToInt("III") == 3
    assert romanToInt("IV") == 4
    assert romanToInt("V") == 5
    assert romanToInt("IX") == 9
    assert romanToInt("LVIII") == 58