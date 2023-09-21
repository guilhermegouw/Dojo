def reverseWordsInString(string):
    reversed_copy_string = string[::-1]
    string_words = string.split()
    reversed_copy_string_words = reversed_copy_string.split()
    reversed_string = reversed_copy_string
    string_words_index = -1
    for i in range(len(string_words)):
        reversed_string = reversed_string.replace(reversed_copy_string_words[i], string_words[string_words_index], 1)
        string_words_index -= 1
    return reversed_string        
