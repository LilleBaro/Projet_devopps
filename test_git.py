from abc import abstractmethod,ABC  

class Employe(ABC):
    def __init__(self,matricule,nom,prenom,date_de_naissance):
        self.matricule=matricule
        self.nom=nom
        self.prenom=prenom
        self.date_de_naissance=date_de_naissance

    @abstractmethod    
    def GetSalaire(self):
        pass

class Ouvrier(Employe):
    SMIG=2500 
    date_actuelle=2023
    def __init__(self,matricule,nom,prenom,date_de_naissance,date_join):
        super(). __init__(matricule,nom,prenom,date_de_naissance)
        self.date_join=date_join
    def GetSalaire(self):
        salaire= Ouvrier.SMIG + (Ouvrier.date_actuelle-self.date_join)*100
        if salaire <= Ouvrier.SMIG*2:
            return f"Le salaire de {self.prenom} {self.nom} est de {salaire}"
        else:
            raise ValueError("Ce salaire est impossible pour un employer")
        
class Cadre(Employe):
    def __init__(self,matricule,nom,prenom,date_de_naissance,indice):
        super().__init__(matricule,nom,prenom,date_de_naissance)
        self.indice=indice
    def GetSalaire(self):
        if self.indice == 1:
            return f"Le salaire de {self.prenom} {self.nom} est de 130000"
        elif self.indice==2:
            return f"Le salaire de {self.prenom} {self.nom} est de 150000"
        elif self.indice==3:
            return f"Le salaire de {self.prenom} {self.nom} est de 170000"
        elif self.indice==4:
            return f"Le salaire de {self.prenom} {self.nom} est de 20000"
        else:
            raise ValueError("Cette indice n'existe pas")

class Patron(Employe):
    chiffre_aff=200000
    def __init__(self,matricule,nom,prenom,date_de_naissance,pourcentage):
        super().__init__(matricule,nom,prenom,date_de_naissance)
        self.pourcentage=pourcentage
    def GetSalaire(self):
        salaire=Patron.chiffre_aff*(self.pourcentage/100)
        return f"Le salaire de {self.prenom} {self.nom} est de {salaire}"


Ouv_1=Ouvrier(321,"De la Fistiniere","Robert","12/02/1980",2000)
Ouv_1.GetSalaire()

Ca1=Cadre(32,"Tuceki","George","12/09/1970",4)
Ca1.GetSalaire()

Pat_1=Patron(4313,"Mbengue","Mohamed Lamine","15/05/2002",50)
Pat_1.GetSalaire()

