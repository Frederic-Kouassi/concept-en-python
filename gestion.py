from livre import Livre
import json


class Bibliotheque:
    def __init__(self):
        self.livres = []

    def ajouter_livres(self, *livres):
        for livre in livres:
            self.livres.append(livre)

    def lister_disponibles(self):
        livre_disponibles = [livre for livre in self.livres if livre.disponible]
        if not livre_disponibles:
            print("Aucun livre disponible")
        for livre in  livre_disponibles:
            print(livre)

    def trouver_livre(self, titre):
        for livre in self.livres:
            if livre.titre.lower() == titre.lower():
                return livre
        raise ValueError("ce livre n'est pas present")

    def emprunter_livre(self, titre):
        livre = self.trouver_livre(titre)
        if not livre.disponible:
            raise Exception("Livre déjà emprunté")
        livre.disponible = False
        print("Livre emprunté avec succès.")

    def rendre_livre(self, titre):
        livre = self.trouver_livre(titre)
        livre.disponible = True
        print("Livre rendu avec succès.")
        
    def suppresion_livre(self, livre):
        for livre in self.livres:
            if livre:
                self.livres.remove(livre)
                print("Le livre a ete supprimer avec succès")
            else:
                print("le livre n'est pas dans la bibliotheque")

    def sauvegarder(self, fichier="data.json"):
        with open(fichier, "w", encoding="utf-8") as f:
            json.dump([livre.to_dict() for livre in self.livres], f, indent=4)

    def charger(self, fichier="data.json"):
        try:
            with open(fichier, "r", encoding="utf-8") as f:
                data = json.load(f)
                self.livres = [Livre.from_dict(l) for l in data]
        except FileNotFoundError:
            self.livres = []


def menu():
    print("\n--- MENU BIBLIOTHÈQUE ---")
    print("1- Ajouter un livre")
    print("2- Lister les livres disponibles")
    print("3- Emprunter un livre")
    print("4- Rendre un livre")
    print("5- Supprimer livre")
    print("6- Quitter et sauvegarder")


def main():
    biblio = Bibliotheque()
    biblio.charger()

    while True:
        menu()
        choix = input("Entrez votre choix parmis les options disponible : ")

        try:
            if choix == "1":
                titre = input("Le Titre : ")
                auteur = input("Auteur : ")
                annee = int(input("Année : "))
                livre = Livre(titre, auteur, annee)
                biblio.ajouter_livres(livre)
                print("Livre ajouté.")

            elif choix == "2":
                biblio.lister_disponibles()

            elif choix == "3":
                titre = input("Titre du livre à emprunter : ")
                biblio.emprunter_livre(titre)

            elif choix == "4":
                titre = input("Titre du livre à rendre : ")
                biblio.rendre_livre(titre)
            
            elif choix == "5":
                titre = input("Titre du livre à supprimer : ")
                biblio.suppresion_livre(titre)

            elif choix == "6":
                biblio.sauvegarder()
                print("Bibliothèque sauvegardée. Au revoir")
                break

            else:
                print("Choix invalide.")

        except ValueError as e:
            print("Erreur :", e)
        except Exception as e:
            print("Erreur :", e)


if __name__ == "__main__":
    main()
