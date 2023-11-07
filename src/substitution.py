def encryption_substitution(text):
    words = text.split()
    list_index = []
    dico = {}
    i = 0

    for word in words:
        if word not in dico.values():
            dico[i] = word
            i += 1

    inverse_dico = {value: key for key, value in dico.items()}

    for word in words:
        list_index.append(inverse_dico[word])

    return list_index, dico

def decryption_substitution(list_index, dico):
    decrypted_words = []
    for index in list_index:
        decrypted_words.append(dico[index])

    return " ".join(mots_decrypte)
