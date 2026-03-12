class Employe:
    def __init__(self, numeroPermis, nom, prenom, voitureService):
        self.numeropermis = numeroPermis
        self.nom = nom
        self.prenom = prenom
        self.voitureService=None
    def afficherInformations(self):
        print(f"Employe: {self.numeropermis} {self.nom} {self.prenom} {self.voitureService}")
        if self.voitureService:
            print(f"voiture service attribue")
            self.voitureService.afficherInformations()
        else:
            print(f"voiture pas attribuee")





