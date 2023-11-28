class type_cuisine:
    '''
    Classe utilisée pour initialiser un type de cuisine
    '''
    def __init__(self, id: str, nom: str, idService: str):
        '''
        Initialise un type de cuisine avec un identifiant, un nom et un identifiant de service.

        PRE : id, nom et idService doivent être des chaînes de caractères non vides.
        POST : Assignation des valeurs d'entrée aux attributs correspondants.
        '''
        self._idCuisine = id
        self._nomTypeCuisine = nom
        self._idService = idService

    '''
    :rest: utilisé pour la sécurité des attributs
    '''
    @property
    def idCuisine(self):
        '''
        Obtient l'identifiant de la cuisine.

        PRE : -
        POST : Renvoie l'identifiant de la cuisine.
        '''
        return self._idCuisine

    @idCuisine.setter
    def idCuisine(self, value):
        '''
        Définit un nouvel identifiant de cuisine.

        PRE : value doit être une chaîne de caractères non vide.
        POST : Assignation de la nouvelle valeur à l'attribut de l'identifiant de cuisine.
        '''
        self._idCuisine = value

    @property
    def nomTypeCuisine(self):
        '''
        Obtient le nom du type de cuisine.

        PRE : -
        POST : Renvoie le nom du type de cuisine.
        '''
        return self._nomTypeCuisine

    @nomTypeCuisine.setter
    def nomTypeCuisine(self, value):
        '''
        Définit un nouveau nom pour le type de cuisine.

        PRE : value doit être une chaîne de caractères non vide.
        POST : Assignation de la nouvelle valeur à l'attribut du nom du type de cuisine.
        '''
        self._nomTypeCuisine = value

    @property
    def idService(self):
        '''
        Obtient l'identifiant de service.

        PRE : -
        POST : Renvoie l'identifiant de service.
        '''
        return self._idService

    @idService.setter
    def idService(self, value):
        '''
        Définit un nouvel identifiant de service.

        PRE : value doit être une chaîne de caractères non vide.
        POST : Assignation de la nouvelle valeur à l'attribut de l'identifiant de service.
        '''
        self._idService = value

    def __str__(self):
        '''
        Renvoie une représentation textuelle du type de cuisine.

        PRE : -
        POST : Renvoie une chaîne de caractères représentant l'identifiant de la cuisine, le type de cuisine et l'identifiant de service.
        '''
        return f"Identifiant cuisine : {self.idCuisine}, Type de cuisine : {self.nomTypeCuisine}, Identifiant service : {self.idService}"
