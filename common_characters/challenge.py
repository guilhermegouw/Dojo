def commonCharacters(strings):
    common = []
    for char in strings[0]:
        if all(char in string for string in strings):
            common.append(char)
    return common
