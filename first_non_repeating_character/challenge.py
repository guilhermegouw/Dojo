def firstNonRepeatingCharacter(string):
    for char in string:
        if string.count(char) == 1:
            return string.index(char)
    return -1