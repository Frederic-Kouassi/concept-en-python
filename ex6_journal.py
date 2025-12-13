
with open("notes.txt", "w") as fichier:
    fichier.write("12\n")
    fichier.write("8\n")
    fichier.write("15.5\n")
    fichier.write("9\n")
    fichier.write("10\n")


with open("notes.txt", "r") as fichier:
    for ligne in fichier:
        note = float(ligne.strip())
        if note >= 10:
            print(note)


def diviser(a, b):
    try:
        a = float(a)
        b = float(b)
        resultat = a / b

    except ZeroDivisionError:
        return "Erreur : division par zéro impossible."

    except ValueError:
        return "Erreur : a ou b n’est pas un nombre."

    else:
        return f"Résultat : {resultat}"

    finally:
        print("Terminer")



print(diviser(10, 2))
print(diviser(10, 0))
print(diviser("abc", 5))
