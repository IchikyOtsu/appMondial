import argparse
class Reservation:
    def __init__(self, nom="", type="", heure="19:00", nbrPers=1, numTable = 0, pmr=0, baby=0):
        self.nom = nom
        self.type = type
        self.heure = heure
        self.nbrPers = nbrPers
        self.numTable = numTable
        self.pmr = pmr
        self.baby = baby

    def modifierNom(self,newNom):
        self.nom = newNom
        return self.nom

    def modifierType(self,newType):
        self.type = newType
        return self.type

    def modifierHeure(self,newHeure):
        self.heure = newHeure
        return self.heure

    def modifierPersonne(self,newNbr):
        self.nbrPers=newNbr
        return self.nbrPers

    def modifierTable(self,newTable):
        self.numTable = newTable
        return self.numTable

    def modifierPMR(self,newPmr):
        self.pmr = newPmr
        return self.pmr

    def modifierBaby(self,newBaby):
        self.baby = newBaby
        return self.baby

    def __str__(self):
        return f"Reservation au nom de {self.nom} à {self.heure} du type {self.type},avec {self.nbrPers} personne(s) dont {self.pmr} personne(s) à mobilité réduite et {self.baby} bébé(s) à la table {self.numTable}"

liste_reservations = []
liste_tables = []
def ajouterReservation(nom="", type="", heure="19:00", nbrPers=1, numTable = 0, pmr=0, baby=0):
    reservation = Reservation(nom, type, heure, nbrPers, numTable, pmr, baby)
    #print(reservation.numTable)
    dico={}
    dico["table"] = reservation.numTable
    dico[reservation.numTable] = reservation
    if dico["table"] not in liste_tables:
        liste_tables.append(dico["table"])
        liste_reservations.append(dico)
    else:
        print(f"ATTENTION la table {dico['table']} est deja réservée !")

    return liste_reservations

def afficheReservations():
    for reservation in liste_reservations:
        print(reservation[reservation["table"]])


parser = argparse.ArgumentParser(prog="Reservation",description="Prends les reservations pour le restaurant")
parser.add_argument("-n", "--nom")
parser.add_argument("-t", "--type")
parser.add_argument("-d","--date")
parser.add_argument("-nbr", "--nombreClient")
parser.add_argument("-pmr","--PMR")
parser.add_argument("-bb","--bébé")
parser.add_argument("-tb","--numTable")
'''
parser.add_argument("type")
parser.add_argument("date")
parser.add_argument("nombreClient")
parser.add_argument("numTable")
'''
args = parser.parse_args()
#ajouterReservation("Mich","VIP","19:00",2,12)
ajouterReservation(args.nom, args.type, args.date, args.nombreClient, args.numTable, args.PMR, args.bébé)
afficheReservations()


