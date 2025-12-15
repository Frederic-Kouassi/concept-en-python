try:
    note = float(input("Entrez une note sur 20 : "))

    if note >= 16:
        print("Très bien")
    elif 14 <= note <= 15:
        print("Bien")
    elif 12 <= note <= 13:
        print("Assez bien")
    elif 10 <= note <= 11:
        print("Moyen")
    else:
        print("Insuffisant")

except ValueError:
    print("Erreur : veuillez entrer un nombre valide.")
