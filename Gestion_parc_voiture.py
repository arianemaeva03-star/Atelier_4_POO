class Voiture:
    def __init__(self, matricule, annee, marque, kilometrage):
        self.matricule = matricule
        self.annee = annee
        self.marque = marque
        self.kilometrage = kilometrage
        self.chauffeur = None
    def afficherInformations(self):
        print(f"Employe: {self.matricule} {self.annee} {self.marque} {self.kilometrage} ")
        if self.chauffeur :
            print(f"chauffeur:{self.chauffeur.nom}")
        else:
            print(f"aucun chauffeur")
class Employe:
    def __init__(self, numeroPermis, nom, prenom,):
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
    def affecterVoitureService(self, VoitureService):
        if VoitureService != None:
            print(f"l'employe a deja une voiture de service")
            return
        if (VoitureService!= None):
           print(f"la voiture est deja attribue")
        self.voitureService = VoitureService
        Voiture.chauffeur = self
        print(f"voiture de service attribue")
    def retirerVoitureService(self, voitureService):
        if self.voitureService == None:
            print(f"l'employe n'a pas de voiture de service")
            return
        self.voitureService = voitureService
        self.voitureService == None
        self.VoitureVoiture.chauffeur = None
        print(f"la Voiture de service peut sortir")
e1=Employe("NP542368", "Diffo", "Maeva")
e2=Employe("NP365842", "Tsafack", "Ariane")

v1=Voiture("ACQ145", "2010", "Toyota", "100000k")
v2=Voiture("PGE148", "2019", "Mercedes", "120000k")
e1.affecterVoitureService(v1)
e2.affecterVoitureService(v2)
e1.afficherInformations()
e2.afficherInformations()
e1.retirerVoitureService(v1)
e1.afficherInformations()













