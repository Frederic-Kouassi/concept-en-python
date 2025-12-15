from utils import calcul_moyenne, trier_liste

listes = []

while 1:
    print("\n--- MENU ---")
    print("1. Ajouter une note")
    print("2. Calculer la moyenne")
    print("3. Trier et afficher les notes")
    print("4. Quitter")

    choix = input("Choisissez une option : ")

    if choix == "1":
        try:
            note = float(input("Entrez une note : "))
            listes.append(note)
            print("la note a bien ete ajoutée.")
        except ValueError:
            print("Erreur : veuillez entrer un nombre.")

    elif choix == "2":
        moyenne = calcul_moyenne(listes)
        print(f"Moyenne des notes : {moyenne}")

    elif choix == "3":
        notes_triees = trier_liste(listes)
        print("Notes triées :", notes_triees)

    elif choix == "4":
        print("Au revoir ")
        break

    else:
        print("Choix invalide.")
