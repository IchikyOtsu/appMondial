from datetime import datetime
class Reservation:
    '''
    class used to init a new reservation for a restaurant
    '''
    def __init__(self, nom : str , telNum, numTable, dateHeure, idCuisine, pmr=0, bb=0, nbrClient =1,idRes = 1):
        '''
        pre :
            -nom : doit être un str
            -telNum : doit être un str
            -numTable : doit être un chiffre strictement plus grand que 0
            #-dateHeure : doit être une date sous forme "annee-mois-hour heure:minute" (deja vérifier dans une autre fonction
            -idCuisine : doit être une chaine de caractère qui est égal a eu , azy , af , an , VIP ou as
            -pmr : doit être un chiffre plus grand ou égal a 0
            -bb : doit être un chiffre plus grand ou égal a 0
            -nbrClient : doit être un chiffre strictement plus grand que 1
            -idRes : doit être un chiffre strictement plus grand que 0

        post :Initialise des données a une instance
        '''
        assert isinstance(nom, str), "le nom doit etre une chaine de charactères."
        assert isinstance(telNum, str), "Le numero de telephone est invalide. Veuiller utiliser une chaine de caractère."
        #assert isinstance(datetime.strptime(dateHeure, "%Y-%m-%d %H:%M"),datetime), "La date doit est sous forme de année-mois-jour heure:minute ."
        assert isinstance(numTable, int) and numTable > 0, "La table doit est un chiffre strictement positif."
        assert isinstance(idCuisine, str) and idCuisine in ["eu", "azy", "af", "as", "an", "VIP"], "L'id cuisine doit être sous forme de deux lettre qui represente une cuisine du monde. Exemple eu,az,af,an,as."
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
        post :affiche un Object de toutes les donnes de l'instance Reservation
        '''
        return f"ID: {self.idRes} nom :{self.nom}, telNum :{self.telNum}, numTable :{self.numTable}, dateHeure :{self.dateHeure}, idCuisine :{self.idCuisine}, pmr :{self.pmr}, bb :{self.bb}, nombre de personne :{self.nbrClient}"
    '''
    :rest == modification of attribut 
    '''
    @property
    def nom(self):
        return self.__nom
    @nom.setter
    def nom(self,  new_nom: str):
        '''
        pre: new_nom doit être une chaine de caractère
        post: modification du nom de l'instance Reservation
        '''
        #assert isinstance(new_nom,str) , "Le nom n'est pas un chaine de character."

        if not isinstance(new_nom, str):
            raise TypeError("Le nom n'est pas une chaîne de caractères.")
        self.__nom = new_nom

    @property
    def idRes(self):
        return self.__idRes

    @idRes.setter
    def idRes(self, new_idRes):
        '''
        pre: new_idRes doit être un chiffre strictement plus grand que 0
        post: modification de l'id de Reservation de l'instance de Reservation
        '''
        #assert isinstance(new_idRes, int) and new_idRes > 0, "Le id n'est pas un int supperieur a 0."
        if not isinstance(new_idRes,int):
            raise TypeError("l'idRes doit etre un chiffre")
        if not (isinstance(new_idRes,int) and new_idRes > 0):
            raise ValueError("l'idRes doit être strictement plus grand que 0")
        self.__idRes = new_idRes

    @property
    def telNum(self):
        return self.__telNum
    @telNum.setter
    def telNum(self, new_telNum):
        '''
        pre: new_telNum doit être une chaine de caractère
        post: modification du numéro de téléphone de l'instance Reservation
        '''
        #assert isinstance(new_telNum,str), "Le numero de telephone est invalide. Veuiller utiliser le +32 si le numéro est belge."
        if not isinstance(new_telNum, str):
            raise TypeError("le numero de telephone doit être une chaine de caractère")
        self.__telNum = new_telNum

    @property
    def numTable(self):
        return self.__numTable
    @numTable.setter
    def numTable(self, new_numTable):
        '''
         pre: new_numTable doit être un chiffre strictement plus grand que 0
         post: modification du numéro de table attribué a la Reservation
        '''
        #assert isinstance(new_numTable, int) and new_numTable > 0, "La table doit est un chiffre strictement positif."

        if not isinstance(new_numTable,int):
            raise TypeError("le numTable doit être un chiffre")
        if not (isinstance(new_numTable,int) and new_numTable>0):
            raise ValueError("le numTable doit être un chiffre strictement plus grand que 0")
        self.__numTable = new_numTable


    @property
    def nbrClient(self):
        return self.__nbrClient

    @nbrClient.setter
    def nbrClient(self, new_nbrClient):
        '''
         pre: new_nbrClient doit être un chiffre plus grand ou égal a 1
         post: modification du nombre de client attribé a une Reservation
        '''
        #assert isinstance(new_nbrClient, int) and new_nbrClient > 0, "La nbr client doit est un chiffre strictement positif."

        if not isinstance(new_nbrClient,int):
            raise TypeError("le nbrClient doit être un chiffre")
        if not (isinstance(new_nbrClient,int) and len(new_nbrClient) >= 1):
            raise ValueError("le nbrClient doit être un chiffre plus grand ou égale a 1")
        self.__numTable = new_nbrClient


    @property
    def dateHeure(self):
        return self.__dateHeure
    @dateHeure.setter
    def dateHeure(self, new_dateHeure):
        '''
        pre: --
        post: initialise une nouvelle date et heure a l'instance
        '''
        #assert isinstance(datetime.strptime(new_dateHeure, "%m/%d/%Y %H:%M"),datetime), "La date doit est sous forme de mois/jour/année heure:minute ."
        self.__dateHeure = new_dateHeure


    @property
    def idCuisine(self):
        return self.__idCuisine
    @idCuisine.setter
    def idCuisine(self, new_idCuisine):
        '''
        pre: idCuisine doit être une chaine de caractère compris entre eu,azy,af,as,an OU VIP
        post: Modification de l'id Cuisine de la reservation
        '''
        #assert isinstance(new_idCuisine, str) and len(new_idCuisine) == 2, "L'id cuisine doit être sous forme de deux lettre qui represente une cuisine du monde. Exemple eu,az,af,an,as."

        if not isinstance(new_idCuisine, str):
            raise TypeError("idCuisine est un chaine de caractère")
        if not (isinstance(new_idCuisine, str) and new_idCuisine == "eu" and new_idCuisine == "azy" and new_idCuisine == "af" and new_idCuisine == "as" and new_idCuisine == "an" and new_idCuisine == "VIP"):
            raise ValueError("idCuisine est un chaine de caractère qui est égal a eu , azy , af , VIP, an ou as")
        self.__idCuisine = new_idCuisine


    @property
    def pmr(self):
        return self.__pmr
    @pmr.setter
    def pmr(self, new_pmr):
        '''
        pre: pmr doit être un chiifre plus grand ou égale a 0
        post: modification du nombre de PMR dans la Reservation
        '''
        #assert isinstance(new_pmr, int) and new_pmr >= 0, "Il faut indiquer le nombre de personne pmr."

        if not isinstance(new_pmr,int):
            raise TypeError("les pmr doit être un chiffre.")
        if not (isinstance(new_pmr,int) and new_pmr >= 0):
            raise ValueError("les pmr doit être un chiffre plus grand ou égal à 0.")
        self.__pmr = new_pmr


    @property
    def bb(self):
        return self.__bb
    @bb.setter
    def bb(self, new_bb):
        '''
         pre: bb doit être un chiifre plus grand ou égale a 0
         post: modification du nombre de bb dans la Reservation
        '''
        #assert isinstance(new_bb, int) and new_bb >= 0, "Il faut indiquer le nombre de bb."

        if not isinstance(new_bb,int):
            raise TypeError("bb doit etre un chiffre.")
        if not (isinstance(new_bb,int) and new_bb >= 0):
            raise ValueError("bb doit etre un chiffre plus grand ou egale à 0.")
        self.__bb = new_bb
    
    def to_json(self):
        # Convertir les attributs du type de service en un dictionnaire JSON
        return {
            "nom": self.nom,
            "telNum": self.telNum,
            "numTable": self.numTable,
            "dateHeure": self.dateHeure,
            "idCuisine": self.idCuisine,
            "pmr": self.pmr,
            "bb": self.bb,
            "nbrClient": self.nbrClient,
            "idRes": self.idRes
        }

    @classmethod
    def from_json(cls, data):
        # Créez une instance de TypeService à partir d'un dictionnaire JSON
        return cls(
            nom=data.get("nom"),
            telNum=data.get("telNum"),
            numTable=data.get("numTable"),
            dateHeure=data.get("dateHeure"),
            idCuisine=data.get("idCuisine"),
            pmr=data.get("pmr"),
            bb=data.get("bb"),
            nbrClient=data.get("nbrClient"),
            idRes=data.get("idRes")
        )