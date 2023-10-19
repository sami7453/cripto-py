from affine import encryption_affine, decryption_affine
from cesar import encryption_cesar, decryption_cesar, craquage

def main_program():
    print("Choisissez un algorithme:")
    print("1. César")
    print("2. Affine")
    print("3. Substitution")

    choice = input("Entrez le numéro de votre choix: ")

    if choice == "1":
        decalage = int(input("Entrez le décalage pour l'algorithme de César: "))
    elif choice == "2":
        a = int(input("Entrez la clé 'a' pour l'algorithme affine: "))
        b = int(input("Entrez la clé 'b' pour l'algorithme affine: "))
    elif choice == "3":
        print("Note: Pour l'algorithme de substitution, vous pouvez seulement chiffrer le texte.")

    if choice in ["1", "2"]:
        action = input("Souhaitez-vous chiffrer ou déchiffrer? (c/d): ")
    else:
        action = "c"

    text = input("Entrez le texte: ")

    try:
        if choice == "1":
            if action == "c":
                result = encryption_cesar(text, decalage)
            else:
                result = decryption_cesar(text, decalage)
        elif choice == "2":
            if action == "c":
                result = encryption_affine(text, a, b)
            else:
                result = decryption_affine(text, a, b)
        elif choice == "3":
            # Ici, vous devez ajouter la fonction de chiffrement de substitution si vous l'avez.
            pass

        print(f"Résultat: {result}")

    except Exception as e:
        print(f"Erreur: {e}")

    again = input("Souhaitez-vous exécuter le programme à nouveau? (o/n): ")

    if again.lower() == "o":
        main_program()

if __name__ == "__main__":
    main_program()
