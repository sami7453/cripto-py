def chiffrement_personnalise(texte):
    cle = 5
    texte_chiffre = ""
    for caractere in texte:
        if caractere.isalpha():
            decale = ord(caractere) + cle
            if caractere.islower():
                if decale > ord('z'):
                    decale -= 26
                elif decale < ord('a'):
                    decale += 26
            elif caractere.isupper():
                if decale > ord('Z'):
                    decale -= 26
                elif decale < ord('A'):
                    decale += 26
            caractere_chiffre = chr(decale)
            texte_chiffre += caractere_chiffre
        else:
            texte_chiffre += caractere
    print("Chaîne chiffrée :", texte_chiffre)
    return texte_chiffre

texte_clair = "Ceci est un exemple de chiffrement simple."
chiffrement_personnalise(texte_clair)

