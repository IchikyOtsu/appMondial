class ReservationManager:
    def __init__(self):
        self.reservations = []
    def addReservation(self,addRes):
        self.reservations.append(addRes)
    def affichage(self):
        for i in self.reservations:
            print(i)
    def removeReservation(self ,rmvRes):
        self.reservations.remove(rmvRes)
    def findReservationByName(self ,nom):
        for i in self.reservations:
            if i.nom == nom:
                return i
