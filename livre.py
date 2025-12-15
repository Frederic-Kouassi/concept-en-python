class Livre:
    def __init__(self, titre, auteur, annee, disponible=True):
        self.titre = titre
        self.auteur = auteur
        self.annee = annee
        self.disponible = disponible

    def to_dict(self):
        return {
            "titre": self.titre,
            "auteur": self.auteur,
            "annee": self.annee,
            "disponible": self.disponible
        }

   
    def from_dict(data):
        
        return Livre(
            data["titre"],
            data["auteur"],
            data["annee"],
            data["disponible"]
        )

    def __str__(self):
        statut = "livre disponible" if self.disponible else "livre emprunté"
        return f"{self.titre} - {self.auteur} ({self.annee})  {statut}"