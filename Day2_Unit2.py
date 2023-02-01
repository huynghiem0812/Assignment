def minion_game(string):
    vowels = "aeiou"
    kevin_vowels = 0
    stuart_consonants = 0
    n = len(string)
    for i in range(n):
        letter = string[i].lower()
        letters_remaining = n - i
        if letter in vowels:
            kevin_vowels += letters_remaining
        else:
            stuart_consonants += letters_remaining

    if stuart_consonants == kevin_vowels:
        print("Draw")
    elif stuart_consonants > kevin_vowels:
        print("Stuart", stuart_consonants)
    else:
        print("Kevin", kevin_vowels)


print(minion_game("BANANA"))
