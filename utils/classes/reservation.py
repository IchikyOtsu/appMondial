class Reservation:
    '''
    class used to init a new reservation for a restaurant 
    '''
    def __init__(self,nom:str,telNum:str,numTable:int,dateHeure:str,idCuisine:int,pmr =0,bb =0,nbrClient = 1,idReservation = 1):
        '''
            pre :nom == str
                telNum == str
                numTable == int and numTable > 0
                dateHeure == datetime
                idCuisine == str and len(idCuisine) == 2
                pmr == int and pmr >= 0
                bb == int and bb >= 0
                idRes == int and idRes > 0

                numTable,pmr et bb ne peuvent pas être négatif.
            post :Initialise des données a une instance
        '''
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
        '''
        pre : --
        post :affiche un Object de toutes les donnes de l'instance
        '''
        return f"ID: {self.idRes} nom :{self.nom}, telNum :{self.telNum}, numTable :{self.numTable}, dateHeure :{self.dateHeure}, idCuisine :{self.idCuisine}, pmr :{self.pmr}, bb :{self.bb}, nombre de personne :{self.nbr}"
    '''
    :rest == modification of attribut 
    '''
    @property
    def nom(self):
        return self.__nom
    @nom.setter
    def nom(self,new_nom):
        '''
        pre: new_nom == str
        post: initialise un nouveau nom a l'instance
        '''
        self.__nom = new_nom

    @property
    def idRes(self):
        return self.__idRes

    @idRes.setter
    def idRes(self, new_id):
        '''
        pre: new_idRes == int and new_idRes > 0
        post: initialise un nouveau idRes a l'instance
        '''
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
        '''
        pre: new_telNum == str
        post: initialise un nouveau numero de telephone a l'instance
        '''
        self.__telNum = new_telNum

    @property
    def numTable(self):
        '''
        pre: numTable == int and numTable > 0
        post: initialise une nouvelle table a l'instance
        '''
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
