class type_cuisine:
    '''
    class used to init a type of cuisine
    '''
    def __init__(self,id : int ,type : str,idService : str):
        self._idCuisine = int(id)
        self._nomTypeCuisine = type
        self._idService = idService
    '''
    :rest: used for security of the attributes
    '''
    @property
    def idCuisine(self):
        return self._idCuisine
    @idCuisine.setter
    def idCuisine(self,value):
        self._idCuisine=value
        
    @property
    def nomTypeCuisine(self):
        return self._nomTypeCuisine
    @nomTypeCuisine.setter
    def nomTypeCuisine(self,value):
        self._nomTypeCuisine=value
    
    @property
    def idService(self):
        return self._idService
    @idService.setter
    def idService(self,value):
        self._idService=value
        
    def __str__(self):
        return f"Identifiant cuisine : {self.idCuisine}, Type de cuisine:{self.nomTypeCuisine}, Identifiant service : {self.idService}"

