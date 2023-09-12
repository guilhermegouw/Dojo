def semordnilap(words):
    semordnilap_pairs = []
    for word in words:
        cleaned_words = words.copy()
        cleaned_words.remove(word)
        if word[::-1] in cleaned_words:
            if (
                [word, word[::-1]] not in semordnilap_pairs and
                [word[::-1], word] not in semordnilap_pairs
            ): semordnilap_pairs.append([word, word[::-1]])
    return semordnilap_pairs
