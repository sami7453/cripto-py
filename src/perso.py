# Chiffrement qui prend en compte une chaine de caractère, une cle et un paterne. La cle est le décalage et le paterne
# est au bout de combien de caractère on change le sens du décalage en passant du + au - et du - au +...

def encryption_perso(texte, cle, paterne):
    texte_chiffre = ""
    decalage = 0
    changer_de_sens = False

    for i in range(len(texte)):
        caractere = texte[i]
        if 'a' <= caractere <= 'z':
            if changer_de_sens:
                decalage = -cle
            else:
                decalage = cle
            caractere_chiffre = chr(((ord(caractere) - ord('a') + decalage) % 26) + ord('a'))
        elif 'A' <= caractere <= 'Z':
            if changer_de_sens:
                decalage = -cle
            else:
                decalage = cle
            caractere_chiffre = chr(((ord(caractere) - ord('A') + decalage) % 26) + ord('A'))
        else:
            caractere_chiffre = caractere

        texte_chiffre += caractere_chiffre

        if (ord(caractere) >= ord('a') and ord(caractere) <= ord('z')) or (ord(caractere) >= ord('A') and ord(caractere) <= ord('Z')):
            if (i + 1) % paterne == 0:
                changer_de_sens = not changer_de_sens
    return texte_chiffre

# Déchiffrement prenant en compte une chaine de caractère, une cle et un paterne. Il s'agit d'une fonction qui déchiffre
# la précédente. Alors si vous souhaiter déchiffrer le texte de la fonction précédente, il faut que la cle et le paterne
# des 2 fonctions soient identiques.

def decryption_perso(texte_chiffre, cle, paterne):
    texte_dechiffre = ""
    decalage = 0
    changer_de_sens = False

    for i in range(len(texte_chiffre)):
        caractere_chiffre = texte_chiffre[i]
        if 'a' <= caractere_chiffre <= 'z':
            if changer_de_sens:
                decalage = -cle
            else:
                decalage = cle
            caractere_dechiffre = chr(((ord(caractere_chiffre) - ord('a') - decalage) % 26) + ord('a'))
        elif 'A' <= caractere_chiffre <= 'Z':
            if changer_de_sens:
                decalage = -cle
            else:
                decalage = cle
            caractere_dechiffre = chr(((ord(caractere_chiffre) - ord('A') - decalage) % 26) + ord('A'))
        else:
            caractere_dechiffre = caractere_chiffre

        texte_dechiffre += caractere_dechiffre

        if (ord(caractere_chiffre) >= ord('a') and ord(caractere_chiffre) <= ord('z')) or (ord(caractere_chiffre) >= ord('A') and ord(caractere_chiffre) <= ord('Z')):
            if (i + 1) % paterne == 0:
                changer_de_sens = not changer_de_sens
    return texte_dechiffre
