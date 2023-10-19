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
    return encryption_cesar(texte, -decalage)

def craquage(texte_chiffre, mot_clair):
    index_mot_clair = texte_chiffre.find(mot_clair)         # Trouver la première occurrence du mot clair dans le texte chiffré
    if index_mot_clair == -1:
        print("Le mot en clair n'a pas été trouvé dans le texte chiffré.")
        return None
    decalage = ord(texte_chiffre[index_mot_clair]) - ord(mot_clair[0])  # Trouver le décalage

    # Déchiffrer le texte
    texte_final = ""
    for lettre in texte_chiffre:
        if lettre.isalpha():
            minuscule = lettre.islower()
            lettre = lettre.lower()
            alphabet = "abcdefghijklmnopqrstuvwxyz"
            index = alphabet.index(lettre)
            index_final= (index - decalage) % 26
            lettre_final = alphabet[index_decale]
            if minuscule:
                texte_final += lettre_final
            else:
                texte_final += lettre_final.upper()
        else:
            texte_final += lettre
    return texte_final
