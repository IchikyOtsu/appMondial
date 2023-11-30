from utils.classes.reservation import Reservation

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
        assert isinstance(addRes, Reservation), "ce n'est pas une instance de Reservation"
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
        #assert isinstance(rmvRes,Reservation)and rmvRes in self.reservations, "La 'instance doit faire partie de l'instance Reservations et faire partie de la liste."
        try:
            if not (isinstance(rmvRes,Reservation)and rmvRes in self.reservations):
                raise TypeError("l'element entre doit etre une instance de Reservation qui fait partie de la liste reservation.")
            self.reservations.remove(rmvRes)
        except TypeError as e:
            print(e)
    def findReservationByName(self ,nom):
        '''
        :param str nom:
        :find a name in liste
        pre: entre un nom
            nom in self.reservations
            nom == str
        post: retourne l'object
        '''
        try:
            if not isinstance(nom, str):
                raise TypeError("La valeur donnée n'est pas un string")
            for i in self.reservations:

                if i.nom == nom:
                    return i
        except TypeError as e :
            print(e)
        except:
            print("erreur car pas dedans")
    def findReservationByTable(self,table):
        try:
            if not isinstance(table, int):
                raise TypeError("La valeur donnée n'est pas un string . findReservationByTable")
            listeTable = []
            for i in self.reservations:

                if i.numTable == table:
                    listeTable.append(i)


            return listeTable

        except TypeError as e:
            print(e)
        except:
            print("erreur car pas dedans")



    def affichage(self):
        '''
        :print:liste
        pre:--
        post: retour chaque reservations de l'instance
        '''
        for i in self.reservations:
            print(i)