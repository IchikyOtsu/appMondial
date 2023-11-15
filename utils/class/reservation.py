class Reservation:
    '''
    class used to init a new reservation for a restaurant 
    '''
    def __init__(self,nom,telNum,numTable,dateHeure,,nbrPersonne,idCuisine,pmr =None,bb =0):
        self.__nom = nom
        self.__telNum = int(telNum)
        self.__numTable = numTable
        self.__dateHeure = dateHeure
        self.__nbrPersonne = nbrPersonne
        self.__idCuisine = idCuisine
        self.__pmr = pmr
        self.__bb = bb
    def __str__(self):
        return f"nom :{self.nom}, telNum :{self.telNum}, numTable :{self.numTable}, dateHeure :{self.dateHeure}, idCuisine :{self.idCuisine}, pmr :{self.pmr}, bb :{self.bb}"
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
    def nbrPersonne(self):
        return self.__nbrPersonne
    @nbrPersonne.setter
    def nbrPersonne(self,new_nbrPersonne):
        self.__nbrPersonne = new_nbrPersonne
    
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
