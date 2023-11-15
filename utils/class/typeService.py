class TypeService:
    '''
    class used to init the type of the service in a resto
    '''

    def __init__(self,idService,nom,idEtage):
        self.__idService = idService
        self.__nom = nom
        self.__idEtage = idEtage
    def __str__(self):
        return f" idService: {self.__idService}, nom: {self.__nom}, idEtage: {self.__idEtage}"

    '''
    :rest: security and modify
    '''
    @property
    def idService(self):
        return self.__idService
    @idService.setter
    def idService(self, new_idService):
        self.__idService = new_idService

    @property
    def nom(self):
        return self.__nom
    @nom.setter
    def nom(self, new_nom):
        self.__nom = new_nom

    @property
    def idEtage(self):
        return self.__idEtage
    @idEtage.setter
    def idEtage(self, new_idEtage):
        self.__idEtage = new_idEtage
