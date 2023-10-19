from affine import encryption_affine, decryption_affine
from cesar import encryption_cesar, decryption_cesar, craquage
from substitution import encryption_substitution, decryption_substitution
from perso import encryption_perso, decryption_perso

def main_program():
    print("Choisissez un algorithme:")
    print("1. César")
    print("2. Affine")
    print("3. Substitution")
    print("4. Craquage César")
    print("5. Chiffrement libre")

    choice = input("Entrez le numéro de votre choix: ")

    if choice == "1":
        key = int(input("Entrez le décalage pour l'algorithme de César: "))
    elif choice == "2":
        key1 = int(input("Entrez la clé 'a' pour l'algorithme affine: "))
        key2 = int(input("Entrez la clé 'b' pour l'algorithme affine: "))
    elif choice == "3":
        print("Note: Pour l'algorithme de substitution, vous pouvez seulement chiffrer le texte.")
    elif choice == "4":
        key3 = str(input("Entrez le texte chiffré pour l'algorithme césar: "))
        key4 = str(input("Entrez le mot clair pour l'algorithme césar: "))
    elif choice == "5":
        key5 = int(input("Entrez la clé pour l'algorithme libre: "))
        key6 = int(input("Entrez le patern pour l'algorithme libre: "))
    else:
        raise IndexError()

    if choice in ["1", "2", "5"]:
        action = input("Souhaitez-vous chiffrer ou déchiffrer? (c/d): ")
    elif choice == "4":
        action = input("continuer (o/n): ")
    else:
        action = "c"

    text = input("Entrez le texte: ")
   
    try:
        if choice == "1":
            if action == "c":
                result = encryption_cesar(text, key)
            else:
                result = decryption_cesar(text, key)
        elif choice == "2":
            if action == "c":
                result = encryption_affine(text, key1, key2)
            else:
                result = decryption_affine(text, key1, key2)
        elif choice == "3":
            if action == "c":
                list, dict = encryption_substitution(text)
                result = list
        elif choice == "4":
            if action == "o":
                result = craquage(key3,key4)
        elif choice == "5":
            if action == "c":
                result = encryption_perso(text, key5, key6)
            else:
                result = decryption_perso(text, key5, key6)

        print(f"Résultat: {result}")

    except Exception as e:
        print(f"Erreur: {e}")

    again = input("Souhaitez-vous exécuter le programme à nouveau? (o/n): ")

    if again.lower() == "o":
        main_program()

if __name__ == "__main__":
    main_program()
