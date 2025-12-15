try:
    valeur = int(input("Entrez un entier : "))
    if valeur > 0:
        print("positif")
    elif valeur < 0:
        print("négatif")
    else:  
        print("zéro")

except ValueError:
    print("Ce n’est pas un nombre valide")
