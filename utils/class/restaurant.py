class Restaurant:
    '''
    class for list all the etage in a restaurant
    '''
    def __init__(self):
        self.etages = []
    def addEtage(self,new_etage):
        '''
        :param object new_etage:
        :add new_etage in list:
        '''
        self.etages.append(new_etage)
    def removeEtage(self,etage):
        '''
        :param object etage:
        :remove object of the liste:
        '''
        self.etages.remove(etage)
    def findEtageById(self,idEtage):
        '''
        :param str idEtage:
        :find etage by idEtage:
        '''
        for i in self.etages:
            if i.idEtage == idEtage:
                return i
    def afficherEtage(self):
        '''
        :print etage:
        '''
        for i in self.etages:
            print(i)
