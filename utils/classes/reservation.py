from datetime import datetime
class Reservation:
    '''
    class used to init a new reservation for a restaurant
    '''
    def __init__(self, nom : str , telNum, numTable, dateHeure, idCuisine, pmr=0, bb=0, nbrClient =1,idRes = 1):
        '''
        pre :nom == str
            telNum == str
            numTable == int and numTable > 0
            dateHeure == datetime
            idCuisine == str and idCuisine == [eu,azy,af,an,as,VIP]
            pmr == int and pmr >= 0
            bb == int and bb >= 0
            idRes == int and idRes > 0
            nbrClient == int and nbrClient >= 1
        post :Initialise des données a une instance
        '''
        assert isinstance(nom, str), "le nom doit etre une chaine de charactères."
        assert isinstance(telNum, str), "Le numero de telephone est invalide. Veuiller utiliser le +32 si le numéro est belge."
        #assert isinstance(datetime.strptime(dateHeure, "%Y-%m-%d %H:%M"),datetime), "La date doit est sous forme de année-mois-jour heure:minute ."
        assert isinstance(numTable, int) and numTable > 0 , "La table doit est un chiffre strictement positif."
        #assert isinstance(idCuisine, str) and len(idCuisine) == 2 or len(idCuisine) == 3, "L'id cuisine doit être sous forme de deux lettre qui represente une cuisine du monde. Exemple eu,azy,af,an,as,VIP."
        assert isinstance(idCuisine, str) and idCuisine == "eu" and idCuisine == "azy" and idCuisine == "af" and idCuisine == "as" and idCuisine == "an" and idCuisine == "VIP"
        assert isinstance(nbrClient,int) and nbrClient == 2 and nbrClient == 4 and nbrClient == 15, "L'id cuisine doit être sous forme de deux lettre qui represente une cuisine du monde. Exemple eu,az,af,an,as."
        assert isinstance(pmr, int) and pmr >= 0, "Il faut indiquer le nombre de personne pmr."
        assert isinstance(bb, int) and bb >= 0, "Il faut indiquer le nombre de bb."
        assert isinstance(idRes, int) and idRes >= 1, "il faut ajouter un id supperieur a 0."
        assert isinstance(nbrClient, int) and nbrClient >= 1, "il faut metre un chifffre superieur a 1"
        self.__nom = nom
        self.__telNum = telNum
        self.__numTable = numTable
        self.__dateHeure = dateHeure
        self.__idCuisine = idCuisine
        self.__pmr = pmr
        self.__bb = bb
        self.__nbrClient = nbrClient
        self.__idRes = idRes
    def __str__(self):
        '''
        pre : --
        post :affiche un Object de toutes les donnes de l'instance
        '''
        return f"ID: {self.idRes} nom :{self.nom}, telNum :{self.telNum}, numTable :{self.numTable}, dateHeure :{self.dateHeure}, idCuisine :{self.idCuisine}, pmr :{self.pmr}, bb :{self.bb}, nombre de personne :{self.nbrClient}"
    '''
    :rest == modification of attribut 
    '''
    @property
    def nom(self):
        return self.__nom
    @nom.setter
    def nom(self,  new_nom:str):
        '''
        pre: new_nom == str
        post: initialise d'un nouveau nom a l'instance
        '''
        #assert isinstance(new_nom,str) , "Le nom n'est pas un chaine de character."
        try:
            if not isinstance(new_nom, str):
                raise TypeError("Le nom n'est pas une chaîne de caractères.")
            self.__nom = new_nom
        except TypeError as e:
            print(e)
    @property
    def idRes(self):
        return self.__idRes

    @idRes.setter
    def idRes(self, new_idRes):
        '''
        pre: new_idRes == int and new_idRes > 0
        post: initialise un nouveau idRes a l'instance
        '''
        #assert isinstance(new_idRes, int) and new_idRes > 0, "Le id n'est pas un int supperieur a 0."
        try:
            if not isinstance(new_idRes,int):
                raise TypeError("l'idRes doit etre un chiffre")
            if not (isinstance(new_idRes,int) and new_idRes > 0):
                raise ValueError("l'idRes doit être strictement plus grand que 0")
            self.__idRes = new_idRes
        except ValueError as e:
            print(e)
        except TypeError as e:
            print(e)
    @property
    def telNum(self):
        return self.__telNum
    @telNum.setter
    def telNum(self, new_telNum):
        '''
        pre: new_telNum == str
        post: initialise un nouveau numero de telephone a l'instance
        '''
        #assert isinstance(new_telNum,str), "Le numero de telephone est invalide. Veuiller utiliser le +32 si le numéro est belge."
        try:
            if not isinstance(new_telNum, str):
                raise TypeError("le numero de telephone doit être une chaine de caractère")
            self.__telNum = new_telNum
        except TypeError as e:
            print(e)
    @property
    def numTable(self):
        return self.__numTable
    @numTable.setter
    def numTable(self, new_numTable):
        '''
         pre: numTable == int and numTable > 0
         post: initialise une nouvelle table a l'instance
        '''
        #assert isinstance(new_numTable, int) and new_numTable > 0, "La table doit est un chiffre strictement positif."
        try:
            if not isinstance(new_numTable,int):
                raise TypeError("le numTable doit être un chiffre")
            if not (isinstance(new_numTable,int) and new_numTable>0):
                raise ValueError("le numTable doit être un chiffre strictement plus grand que 0")
            self.__numTable = new_numTable
        except (TypeError,ValueError) as e:
            print(e)

    @property
    def nbrClient(self):
        return self.__nbrClient

    @nbrClient.setter
    def nbrClient(self, new_nbrClient):
        '''
         pre: nbrClient == int and nbrClient  >= 1
         post: initialise une nouvelle nbr client a l'instance
        '''
        #assert isinstance(new_nbrClient, int) and new_nbrClient > 0, "La nbr client doit est un chiffre strictement positif."

        try:
            if not isinstance(new_nbrClient,int):
                raise TypeError("le nbrClient doit être un chiffre")
            if not (isinstance(new_nbrClient,int) and len(new_nbrClient) >= 1):
                raise ValueError("le nbrClient doit être un chiffre plus grand ou égale a 1")
            self.__numTable = new_nbrClient
        except (TypeError, ValueError) as e:
            print(e)


    @property
    def dateHeure(self):
        return self.__dateHeure
    @dateHeure.setter
    def dateHeure(self, new_dateHeure):
        '''
        pre: dateHeure == datetime
        post: initialise une nouvelle date et heure a l'instance
        '''
        #assert isinstance(datetime.strptime(new_dateHeure, "%m/%d/%Y %H:%M"),datetime), "La date doit est sous forme de mois/jour/année heure:minute ."
        try:
            if not isinstance(datetime.strptime(new_dateHeure, "%m/%d/%Y %H:%M"),datetime):
                raise ValueError("La date doit est sous forme de année-mois-jour heure:minute .")
            self.__dateHeure = new_dateHeure
        except ValueError as e :
            print(e)

    @property
    def idCuisine(self):
        return self.__idCuisine
    @idCuisine.setter
    def idCuisine(self, new_idCuisine):
        '''
        pre: idCuisine == str and idCuisine == [eu,azy,af,as,an , VIP]
        post: initialise une nouvelle id de cuisine a l'instance
        '''
        #assert isinstance(new_idCuisine, str) and len(new_idCuisine) == 2, "L'id cuisine doit être sous forme de deux lettre qui represente une cuisine du monde. Exemple eu,az,af,an,as."
        try:
            if not isinstance(new_idCuisine, str):
                raise TypeError("idCuisine est un chaine de caractère")
            if not (isinstance(new_idCuisine, str) and new_idCuisine == "eu" and new_idCuisine == "azy" and new_idCuisine == "af" and new_idCuisine == "as" and new_idCuisine == "an" and new_idCuisine == "VIP"):
                raise ValueError("idCuisine est un chaine de caractère qui est égal a eu , azy , af , VIP, an ou as")
            self.__idCuisine = new_idCuisine
        except (TypeError, ValueError) as e:
            print(e)

    @property
    def pmr(self):
        return self.__pmr
    @pmr.setter
    def pmr(self, new_pmr):
        '''
        pre: pmr == int and pmr >= 0
        post: initialise un nouveau nombre de pmr a l'instance
        '''
        #assert isinstance(new_pmr, int) and new_pmr >= 0, "Il faut indiquer le nombre de personne pmr."
        try:
            if not isinstance(new_pmr,int):
                raise TypeError("les pmr doit être un chiffre.")
            if not (isinstance(new_pmr,int) and new_pmr >= 0):
                raise ValueError("les pmr doit être un chiffre plus grand ou égal à 0.")
            self.__pmr = new_pmr
        except (ValueError, TypeError) as e:
            print(e)

    @property
    def bb(self):
        return self.__bb
    @bb.setter
    def bb(self, new_bb):
        '''
        pre: bb == int and bb >= 0
        post initialise un nouveau nombre de bebe a l'instance
        '''
        #assert isinstance(new_bb, int) and new_bb >= 0, "Il faut indiquer le nombre de bb."

        try:
            if not isinstance(new_bb,int):
                raise TypeError("bb doit etre un chiffre.")
            if not (isinstance(new_bb,int) and new_bb >= 0):
                raise ValueError("bb doit etre un chiffre plus grand ou egale à 0.")
            self.__bb = new_bb
        except (TypeError, ValueError) as e:
            print(e)