
class ReservationManager:
    def __init__(self):
        self.reservations = []
    def addReservation(self,addRes):
        '''
        :param str addRes:newReservation
        :add newReservation in liste
        '''
        self.reservations.append(addRes)
    def removeReservation(self ,rmvRes):
        '''
        :param str rmvRes:liste
        :remove a name in liste
        '''
        self.reservations.remove(rmvRes)
    def findReservationByName(self ,nom):
        '''
        :param str nom:
        :find a name in liste
        '''
        for i in self.reservations:
            if i.nom == nom:
                return i
    def affichage(self):
        '''
        :print:liste
        '''
        for i in self.reservations:
            print(i)
