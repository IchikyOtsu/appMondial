class ReservationManager:
    def __init__(self):
        '''
        pre:--
        post: initialisation de l'instance qui comporte une liste
        '''
        self.reservations = []

    def addReservation(self,addRes):
        '''
        :param str addRes:newReservation
        :add newReservation in liste

        pre: addRes == instance de Reservation
        post: ajoute des donnees dans la list de l'instance
        '''
        self.reservations.append(addRes)
    def removeReservation(self ,rmvRes):
        '''
        :param str rmvRes:liste
        :remove a name in liste
        pre: entree une nouvelle instance
            rmvRes in self.reservations
            rmvRes == instance de Reservation
        post: retrait des donnees dans la list de l'instance
        '''
        self.reservations.remove(rmvRes)
    def findReservationByName(self ,nom):
        '''
        :param str nom:
        :find a name in liste
        pre: entre un nom
            nom in self.reservations
            nom == str
        post: retourne l'object
        '''
        for i in self.reservations:
            if i.nom == nom:
                return i

    def findReservationById(self ,id):
        for i in self.reservations:
            if i.idRes == id:
                return i

    def findReservationByTable(self ,id):
        '''
        :param str nom:
        :find a name in liste
        '''
        reserv = []
        for i in self.reservations:
            if i.numTable == id:
                reserv.append(i)
        return reserv
    def affichage(self):
        '''
        :print:liste
        pre:--
        post: retour chaque reservations de l'instance
        '''
        for i in self.reservations:
            print(i)

