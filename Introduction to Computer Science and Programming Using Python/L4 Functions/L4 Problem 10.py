def isVowel(char):
    '''
    char: a single letter of any case

    returns: True if char is a vowel and False otherwise.
    '''
    if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
        return True
    elif char == 'A' or char == 'E' or char == 'I' or char == 'O' or char == 'U':
        return True
    else:
        return False



print(isVowel('u'))
print(isVowel('S'))
print(isVowel('E'))
print(isVowel('N'))
print(isVowel('A'))
print(isVowel('A'))
print(isVowel('B'))
print(isVowel('b'))
print(isVowel('U'))
print(isVowel('O'))