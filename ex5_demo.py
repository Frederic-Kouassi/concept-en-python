
class Voiture:
    def __init__(self, marque, modele, annee, kilometrage):
        self.marque = marque
        self.modele = modele
        self.annee = annee
        self.kilometrage = kilometrage

    def afficher(self):
        print(f"Voiture : {self.marque} {self.modele}, Année : {self.annee}, Kilométrage : {self.kilometrage} km")


class VoitureElectrique(Voiture):
    def __init__(self, marque, modele, annee, kilometrage, autonomie):
        super().__init__(marque, modele, annee, kilometrage)
        self.autonomie = autonomie

   
    def afficher(self):
        super().afficher()  
        print(f"Autonomie : {self.autonomie} km")
        
    
marque= input("entrez le nom de la marque: ")
modele= input("entrez le nom de la modele :")
prix= input("entrez le prix")
kilometrage= input("entrez le kilometrage:")


voiture1 = Voiture(marque, modele, prix, kilometrage)
voiture1.afficher()

print("\n--- Voiture électrique ---")
voiture_elec = VoitureElectrique(marque, modele, prix, kilometrage, 500)
voiture_elec.afficher()
