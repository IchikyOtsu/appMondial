class type_cuisine_manager:
    '''
    Classe utilisée pour initialiser une liste de différents types de cuisine.
    '''

    def __init__(self):
        '''
        Initialise une liste vide de types de cuisine.

        PRE : -
        POST : Crée une liste vide pour stocker les types de cuisine.
        '''
        self._cuisine_list = []

    '''
    :rest: sécurité et modification des attributs
    '''

    @property
    def cuisine_list(self):
        '''
        Récupère la liste des types de cuisine.

        PRE : -
        POST : Renvoie la liste des types de cuisine.
        '''
        return self._cuisine_list

    @cuisine_list.setter
    def cuisine_list(self, value):
        '''
        Définit une nouvelle liste de types de cuisine.

        PRE : value doit être une liste.
        POST : Remplace la liste actuelle par la nouvelle liste spécifiée.
        '''
        if isinstance(value, list):
            self._cuisine_list = value

    '''
    Méthodes utilisées pour ajouter, supprimer et afficher une cuisine de la liste.
    '''

    def addCuisine(self, *reservations):
        '''
        Ajoute des types de cuisine à la liste.

        PRE : Les réservations doivent être des objets de type TypeCuisine non présents dans la liste.
        POST : Ajoute les réservations à la liste des types de cuisine.
        '''
        for reservation in reservations:
            if reservation not in self.cuisine_list:
                self.cuisine_list.append(reservation)

    def removeCuisine(self, *reservations):
        '''
        Supprime des types de cuisine de la liste.

        PRE : Les réservations doivent être des objets de type TypeCuisine présents dans la liste.
        POST : Supprime les réservations de la liste des types de cuisine.
        '''
        for reservation in reservations:
            if reservation in self.cuisine_list:
                self.cuisine_list.remove(reservation)

    def displayList(self):
        '''
        Affiche la liste des types de cuisine.

        PRE : -
        POST : Affiche les informations de chaque type de cuisine dans la liste.
        '''
        if len(self.cuisine_list):
            print("Voici les éléments de la liste")
            for elem in self.cuisine_list:
                print(f"{elem}")

    def findCuisineById(self, id):
        '''
        Recherche un type de cuisine par son identifiant.

        PRE : id doit être une chaîne de caractères correspondant à un identifiant de type de cuisine.
        POST : Renvoie le type de cuisine correspondant à l'identifiant spécifié s'il existe.
        '''
        for i in self.cuisine_list:
            if i.idCuisine == id:
                return i

    def __str__(self):
        '''
        Renvoie une représentation textuelle de la liste de cuisine.

        PRE : -
        POST : Renvoie une chaîne de caractères contenant la liste des types de cuisine.
        '''
        return f"Liste de cuisine : {self._cuisine_list}"