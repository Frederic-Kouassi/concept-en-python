fruits = []
liste = ["1", "2", "3", "4", "5", "6"]

while True:
    print("\nMenu :")
    print("1. Ajouter un fruit")
    print("2. Supprimer un fruit")
    print("3. Rechercher un fruit")
    print("4. Modifier un fruit")
    print("5. Afficher tous les fruits triés avec index")
    print("6. Quitter")

    choix = input("Choisissez une option (1-6) : ")

    while choix not in liste:
        print("Option invalide veuillez choisir un numéro entre 1 et 6.")
        choix = input("Choisissez une option (1-6) : ")

    if choix == "1":
        nouveau_fruit = input("Ajoutez un fruit : ")
        fruits.append(nouveau_fruit)
        print(f"{nouveau_fruit} a été ajouté")

    elif choix == "2":
        suppression = input("Entrez le fruit à supprimer : ")
        if suppression in fruits:
            fruits.remove(suppression)
            print(f"Le fruit '{suppression}' a été supprimé.")
        else:
            print(f"Le fruit '{suppression}' n'est pas dans la liste.")

    elif choix == "3":
        recherche = input("Entrez le fruit à rechercher : ")
        if recherche in fruits:
            print(f"Le fruit recherché est : {recherche}")
        else:
            print(f"Le fruit '{recherche}' n'est pas dans la liste.")

    elif choix == "4":
        ancien = input("Entrez le fruit que vous souhaitez modifier : ")
        if ancien in fruits:
            nouveau = input("Entrez le nouveau nom du fruit : ")
            index = fruits.index(ancien)
            fruits[index] = nouveau
            print(f"'{ancien}' a été remplacé par '{nouveau}'.")
        else:
            print(f"Le fruit '{ancien}' n'est pas dans la liste.")

    elif choix == "5":
        if fruits:
            fruits_tries = sorted(fruits)
            print("Liste triée des fruits avec index :")
            for i, fruit in enumerate(fruits_tries, start=1):
                print(f"{i} - {fruit}")
        else:
            print("La liste est vide")

    elif choix == "6":
        print("Au revoir")
        break
