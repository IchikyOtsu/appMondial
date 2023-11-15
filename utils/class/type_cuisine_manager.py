class type_cuisine_manager:
    '''
    class used to init a list of different type of cuisine
    '''
    def __init__(self):
        self._cuisine_list = []
        
    '''
    :rest: security and modification of attributes
    '''
    @property
    def cuisine_list(self):
        return self._cuisine_list
    
    @cuisine_list.setter
    def cuisine_list(self,value):
        if isinstance(value,list):
            self._cuisine_list = value
    
    '''
    method used to append, remove and display a reservation from the list
    '''
    def addCuisine(self,*reservations):
        for reservation in reservations:
            if reservation not in self.cuisine_list:
                self.cuisine_list.append(reservation)
    def removeCuisine(self,*reservations):
        for reservation in reservations:
            if reservation in self.cuisine_list:
                self.cuisine_list.remove(reservation)     
    def displayList(self):
        if len(self.cuisine_list):
            print("Voici les éléments de la liste")
            for elem in self.cuisine_list:
                    print(f"{elem}")
    
    def __str__(self):
        return f"Liste de cuisine : {self._cuisine_list}"
    
