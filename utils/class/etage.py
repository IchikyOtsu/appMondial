class Etage:
    '''
    class used to init a Etage in a restaurent
    '''
    def __init__(self,idEtage,nom):
        self.__idEtage = idEtage
        self.__nom = nom
    def __str__(self):
        return f"idEtage: {self.__idEtage}, nom: {self.__nom}"
    '''
    :rest: modify and security 
    '''
    @property
    def idEtage(self):
        return self.__idEtage
    @idEtage.setter
    def idEtage(self, new_idEtage):
        self.__idEtage = new_idEtage

    @property
    def nom(self):
        return self.__nom
    @nom.setter
    def nom(self, new_nom):
        self.__nom = new_nom
