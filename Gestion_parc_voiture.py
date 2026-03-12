class Employe:
    def __init__(self, numeroPermis, nom, prenom):
        self.numeropermis = numeroPermis
        self.nom = nom
        self.prenom = prenom
        self.voitureService=None
    def afficherInformations(self):
        print(f"Employe: {self.numeropermis} {self.nom} {self.prenom} ")
        if self.voitureService:
            self.voitureService.afficherInformations()
            print(f"voiture service attribue")
        else:
            print(f"voiture pas attribuee")
    def affecterVoitureService(self, voitureService):
        if self.voitureService != None:
            print(f"l'employe a deja une voiture de service")
            return
        if Voiture.chauffeur != None:
            Print(f"la voiture est deja attribue")
        self.voitureService = voitureService
        Voiture.chauffeur = self
        print(f"voiture de service attribue")
    def retirerVoitureService(self, voitureService):
        if self.voitureService == None:
            print(f"l'employe n'a pas de voiture de service")
            return
        self.voitureService = voitureService
        self.voitureService== None
        Voiture.chauffeur = None
        print(f"la Voiture de service peut sortir")
    class Voiture:
        def __init__(self, matricule, annee, marque, kilometrage,chauffeur):
            self.matricule = matricule
            self.annee = annee
            self.marque = marque
            self.kilometrage = kilometrage
            self.chauffeur = None








