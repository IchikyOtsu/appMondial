class TypeServiceManager:
    def __init__(self):
        '''
        Initialise une liste vide de services.

        PRE : -
        POST : Crée une liste vide pour stocker les services.
        '''
        self.services = []

    def addService(self, new_service):
        '''
        Ajoute un service à la liste.

        PRE : new_service doit être un objet de type TypeService.
        POST : Ajoute le service à la liste des services.
        '''
        self.services.append(new_service)

    def removeService(self, service):
        '''
        Supprime un service de la liste.

        PRE : service doit être un objet de type TypeService présent dans la liste.
        POST : Supprime le service de la liste des services.
        '''
        self.services.remove(service)

    def findServiceById(self, idService):
        '''
        Recherche un service par son identifiant.

        PRE : idService doit être un identifiant valide.
        POST : Affiche les informations du service correspondant à l'identifiant spécifié s'il existe.
        '''
        for i in self.services:
            if i.idService == idService:
                print(i)

    def afficherServices(self):
        '''
        Affiche la liste des services.

        PRE : -
        POST : Affiche les informations de chaque service dans la liste.
        '''
        for i in self.services:
            print(i)
