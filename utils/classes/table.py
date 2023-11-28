class Table:
    '''
    Classe utilisée pour initialiser une nouvelle table
    '''
    def __init__(self, numTable, capaciteTable, idService):
        '''
        Initialise une nouvelle table avec un numéro de table, une capacité et un identifiant de service.

        PRE : numTable, capaciteTable et idService doivent être des entiers.
        POST : Assignation des valeurs d'entrée aux attributs correspondants.
        '''
        self.__numTable = int(numTable)
        self.__capaciteTable = int(capaciteTable)
        self.__idService = idService

    def __str__(self):
        '''
        Renvoie une représentation textuelle de la table.

        PRE : -
        POST : Renvoie une chaîne de caractères contenant le numéro de table, la capacité et l'identifiant de service.
        '''
        return f"numTable: {self.__numTable}, capaciteTable: {self.__capaciteTable}, idService: {self.__idService} "

    '''
    :rest: modification et sécurité
    '''
    @property
    def numTable(self):
        '''
        Obtient le numéro de table.

        PRE : -
        POST : Renvoie le numéro de table.
        '''
        return self.__numTable

    @numTable.setter
    def numTable(self, new_numTable):
        '''
        Définit un nouveau numéro de table.

        PRE : new_numTable doit être un entier.
        POST : Assignation de la nouvelle valeur à l'attribut du numéro de table.
        '''
        self.__numTable = new_numTable

    @property
    def capaciteTable(self):
        '''
        Obtient la capacité de la table.

        PRE : -
        POST : Renvoie la capacité de la table.
        '''
        return self.__capaciteTable

    @capaciteTable.setter
    def capaciteTable(self, new_capaciteTable):
        '''
        Définit une nouvelle capacité de table.

        PRE : new_capaciteTable doit être un entier.
        POST : Assignation de la nouvelle valeur à l'attribut de la capacité de la table.
        '''
        self.__capaciteTable = new_capaciteTable

    @property
    def idService(self):
        '''
        Obtient l'identifiant de service de la table.

        PRE : -
        POST : Renvoie l'identifiant de service de la table.
        '''
        return self.__idService

    @idService.setter
    def idService(self, new_idService):
        '''
        Définit un nouvel identifiant de service pour la table.

        PRE : new_idService doit être un entier.
        POST : Assignation de la nouvelle valeur à l'attribut de l'identifiant de service de la table.
        '''
        self.__idService = new_idService
