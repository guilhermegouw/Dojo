def runLengthEncoding(string):
    encoded = ''
    count = 1
    for i, char in enumerate(string):
        if i == len(string) - 1:
            encoded += str(count) + char
            break
        if char == string[i + 1]:
            if count == 9:
                encoded += str(count) + char
                count = 1
            else:
                count += 1
        else:
            encoded += str(count) + char
            count = 1
    return encoded