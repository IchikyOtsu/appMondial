class TypeServiceManager:
    def __init__(self):
        self.services = []
    def addService(self,new_service):
        '''
        :param object new_service: service
        :add a service in the liste
        '''
        self.services.append(new_service)
    def removeService(self,service):
        '''
        :param object service: service
        :remove a service in the liste
        '''
        self.services.remove(service)
    def findServiceById(self,idService):
        '''
        :param int idService: id
        :find a service in the liste  
        '''
        for i in self.services:
            if i.idService == idService:
                print(i)
    def afficherServices(self):
        '''
        :print liste
        '''
        for i in self.services:
            print(i)
