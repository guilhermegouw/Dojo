def generateDocument(characters, document):
    characters_dict = {}
    document_dict = {}
    for character in characters:
        if character in characters_dict:
            characters_dict[character] += 1
        else:
            characters_dict[character] = 1
    
    for character in document:
        if character in document_dict:
            document_dict[character] += 1
        else:
            document_dict[character] = 1
    
    for key in document_dict:
        if key not in characters_dict:
            return False
        elif document_dict[key] > characters_dict[key]:
            return False
    return True
