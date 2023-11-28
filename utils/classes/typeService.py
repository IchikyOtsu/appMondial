class TypeService:
    '''
    Classe utilisée pour initialiser le type de service dans un restaurant.
    '''

    def __init__(self, idService, nom, idEtage):
        '''
        Initialise le type de service avec un identifiant, un nom et un identifiant d'étage.

        PRE : idService, nom et idEtage doivent être des paramètres valides.
        POST : Crée une instance de TypeService avec les attributs spécifiés.
        '''
        self.__idService = idService
        self.__nom = nom
        self.__idEtage = idEtage

    def __str__(self):
        '''
        Renvoie une représentation textuelle du type de service.

        PRE : -
        POST : Renvoie une chaîne de caractères contenant l'identifiant, le nom et l'identifiant d'étage du service.
        '''
        return f" idService: {self.__idService}, nom: {self.__nom}, idEtage: {self.__idEtage}"

    '''
    :rest: sécurité et modification
    '''

    @property
    def idService(self):
        '''
        Récupère l'identifiant du service.

        PRE : -
        POST : Renvoie l'identifiant du service.
        '''
        return self.__idService

    @idService.setter
    def idService(self, new_idService):
        '''
        Modifie l'identifiant du service.

        PRE : new_idService doit être un identifiant valide.
        POST : Modifie l'identifiant du service avec la nouvelle valeur spécifiée.
        '''
        self.__idService = new_idService

    @property
    def nom(self):
        '''
        Récupère le nom du service.

        PRE : -
        POST : Renvoie le nom du service.
        '''
        return self.__nom

    @nom.setter
    def nom(self, new_nom):
        '''
        Modifie le nom du service.

        PRE : new_nom doit être un nom valide.
        POST : Modifie le nom du service avec la nouvelle valeur spécifiée.
        '''
        self.__nom = new_nom

    @property
    def idEtage(self):
        '''
        Récupère l'identifiant de l'étage associé au service.

        PRE : -
        POST : Renvoie l'identifiant de l'étage associé au service.
        '''
        return self.__idEtage

    @idEtage.setter
    def idEtage(self, new_idEtage):
        '''
        Modifie l'identifiant de l'étage associé au service.

        PRE : new_idEtage doit être un identifiant d'étage valide.
        POST : Modifie l'identifiant de l'étage associé au service avec la nouvelle valeur spécifiée.
        '''
        self.__idEtage = new_idEtage
