
from chiffrement_affine import decryption_affine, encryption_affine
from chiffrement_cesar import chiffrement_cesar, dechiffrement_cesar, craquage
from chiffrement_libre import chiffrement_personnalise
from chiffrement_substitution import chiffrement_substitution, dechiffrement_substitution

def main_program():
    print("Choisissez un algorithme ou une methode:")
    print("1. César")
    print("2. Affine")
    print("3. Substitution")
    print("4. craquage césar")
    print("5. chiffrement libre")
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
        print("Note: Pour l'algorithme libre, vous pouvez seulement chiffrer le texte.")



    if choice in ["1", "2","5"]:
        action = input("Souhaitez-vous chiffrer ou déchiffrer? (c/d): ")
    elif choice in ["4"]:
        action = input("continuer (o/n): ")
    else:
        action = "c"

    text = input("Entrez le texte: ")

    try:
        if choice == "1":
            if action == "c":
                result = chiffrement_cesar(text, key)
            else:
                result = dechiffrement_cesar(text,key)
            pass
        elif choice == "2":
            if action == "c":
                result = encryption_affine(text, key1, key2)
            else:
                result = decryption_affine(text, key1, key2)
        elif choice == "3":
            # Ici, vous devez ajouter la fonction de chiffrement de substitution si vous l'avez.
            pass
        elif choice == "4":
            if action == "o":
                result = craquage(key3,key4)
            else:
                pass
        elif choice == "5":
            result = chiffrement_personnalise(text)
            pass


        print(f"Résultat: {result}")

    except Exception as e:
        print(f"Erreur: {e}")

    again = input("Souhaitez-vous exécuter le programme à nouveau? (o/n): ")
    if again.lower() == "o":
        main_program()

if __name__ == "__main__":
    main_program()
