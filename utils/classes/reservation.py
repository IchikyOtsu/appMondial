class Reservation:
    '''
    class used to init a new reservation for a restaurant 
    '''
    def __init__(self,nom,telNum,numTable,dateHeure,idCuisine,pmr =False,bb =False,nbrClient = 1,idReservation = 1):
        self.__nom = nom
        self.__telNum = int(telNum)
        self.__numTable = numTable
        self.__dateHeure = dateHeure
        self.__idCuisine = idCuisine
        self.__pmr = pmr
        self.__bb = bb
        self.__nbr = nbrClient
        self.__idRes = idReservation

    def __str__(self):
        return f"ID: {self.idRes} nom :{self.nom}, telNum :{self.telNum}, numTable :{self.numTable}, dateHeure :{self.dateHeure}, idCuisine :{self.idCuisine}, pmr :{self.pmr}, bb :{self.bb}, nombre de personne :{self.nbr}"
    '''
    :rest == modification of attribut 
    '''
    @property
    def nom(self):
        return self.__nom
    @nom.setter
    def nom(self,new_nom):
        self.__nom = new_nom

    @property
    def idRes(self):
        return self.__idRes

    @idRes.setter
    def idRes(self, new_id):
        self.__idRes = new_id

    @property
    def nbr(self):
        return self.__nbr

    @nbr.setter
    def nbr(self, newNbr):
        self.__nbr = newNbr

    @property
    def telNum(self):
        return self.__telNum
    @telNum.setter
    def telNum(self, new_telNum):
        self.__telNum = new_telNum

    @property
    def numTable(self):
        return self.__numTable
    @numTable.setter
    def numTable(self, new_numTable):
        self.__numTable = new_numTable

    @property
    def dateHeure(self):
        return self.__dateHeure
    @dateHeure.setter
    def dateHeure(self, new_dateHeure):
        self.__dateHeure = new_dateHeure

    @property
    def idCuisine(self):
        return self.__idCuisine
    @idCuisine.setter
    def idCuisine(self, new_idCuisine):
        self.__idCuisine = new_idCuisine

    @property
    def pmr(self):
        return self.__pmr
    @pmr.setter
    def pmr(self, new_pmr):
        self.__pmr = new_pmr

    @property
    def bb(self):
        return self.__bb
    @bb.setter
    def bb(self, new_bb):
        self.__bb = new_bb
