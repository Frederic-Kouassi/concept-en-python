valeurs = []  

while True:
    entree = input("Entrez un nombre (ou 'stop' pour terminer) : ")

    if entree.lower() == "stop":
        break

    try:
        nombre = float(entree)
        valeurs.append(nombre)
    except ValueError:
        print("Ce n’est pas un nombre valide.")

if len(valeurs) > 0:
    total = sum(valeurs)
    moyenne = total / len(valeurs)

    print("\n----- RÉSULTATS -----")
    print(f"Nombre de valeurs saisies : {len(valeurs)}")
    print(f"Somme : {total}")
    print(f"Moyenne : {moyenne}")
else:
    print("Aucune valeur numérique n'a été saisie.")
