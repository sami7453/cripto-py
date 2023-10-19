def encryption_substitution(texte):
    mots = texte.split()
    list_index = []
    dico = {}
    i = 0

    for mot in mots:
        if mot not in dico.values():
            dico[i] = mot
            i += 1

    inverse_dico = {value: key for key, value in dico.items()}

    for mot in mots:
        list_index.append(inverse_dico[mot])

    return list_index, dico

def decryption_substitution(list_index, dico):
    mots_decrypte = []
    for index in list_index:
        mots_decrypte.append(dico[index])

    phrase = " ".join(mots_decrypte)
    return phrase
