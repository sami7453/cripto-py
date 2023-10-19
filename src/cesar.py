def encryption_cesar(texte, decalage):
    texte_final = ""

    for lettre in texte:
        if lettre.isalpha():                                # Vérifier si la lettre est alphabétique
            minuscule = lettre.islower()                    # Vérifier si la lettre est en minuscule
            lettre = lettre.lower()                         # Convertir en minuscule pour le traitement
            alphabet = "abcdefghijklmnopqrstuvwxyz"         # L'alphabet en minuscules
            index = alphabet.index(lettre)                  # recupère l'index de la lettre 
            index_final = (index + decalage) % 26           # effectue l'opération pour obtenir un nouvel index
            lettre_final = alphabet[index_final]            #nous donne la nouvelle lettre correspondant au nouvel index
            if minuscule:
                texte_final += lettre_final                 #si la nouvelle lettre est une majuscule on l'ajoute tel quelle
            else:
                texte_final += lettre_final.upper()         #sinon on la met en majuscule
        else:
            texte_final += lettre                           # Conserver les caractères non alphabétiques tel quel
    return texte_final

def decryption_cesar(texte, decalage):
    texte_final = ""

    for lettre in texte:
        if lettre.isalpha():                                # Vérifier si la lettre est alphabétique
            minuscule = lettre.islower()                    # Vérifier si la lettre est en minuscule
            lettre = lettre.lower()                         # Convertir en minuscule pour le traitement
            alphabet = "abcdefghijklmnopqrstuvwxyz"         # L'alphabet en minuscules
            index = alphabet.index(lettre)                  # recupère l'index de la lettre 
            index_final = (index - decalage) % 26           # effectue l'opération pour obtenir un nouvel index
            lettre_final = alphabet[index_final]            #nous donne la nouvelle lettre correspondant au nouvel index
            if minuscule:
                texte_final += lettre_final                 #si la nouvelle lettre est une majuscule on l'ajoute tel quelle
            else:
                texte_final += lettre_final.upper()         #sinon on la met en majuscule
        else:
            texte_final += lettre                           # Conserver les caractères non alphabétiques tel quel
    return texte_final

def craquage(texte_chiffre, mot_clair):
    for decalage in range(26):                              # Pour chaque décalage possible
        texte_dechiffre = decryption_cesar(texte_chiffre, decalage)
        if mot_clair in texte_dechiffre:
            print(f"Decalage trouvé : {decalage}")
            print(f"Texte déchiffré : {texte_dechiffre}")
            return decalage
    print("Le mot en clair n'a pas été trouvé dans le texte chiffré.")
    return None
