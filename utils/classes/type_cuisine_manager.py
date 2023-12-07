from utils.classes.type_cuisine import type_cuisine
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

    def addCuisine(self, *newCuisine):
        '''
        Ajoute des types de cuisine à la liste.

        PRE : newCuisine doit être un/des objets de type TypeCuisine non présents dans la liste.
        POST : Ajoute les réservations à la liste des types de cuisine.
        '''
        assert not isinstance(newCuisine, type_cuisine), "l'instance ne fait pas partie de type_cuisine"
        for cuisine in newCuisine:
            if cuisine not in self.cuisine_list:
                self.cuisine_list.append(cuisine)

    def removeCuisine(self, reservations):
        '''
        Supprime des types de cuisine de la liste.

        PRE : Les réservations doivent être des objets de type TypeCuisine présents dans la liste.
        POST : Supprime les réservations de la liste des types de cuisine.
        '''
        try:
            if not (isinstance(reservations, type_cuisine) and reservations in self._cuisine_list):
                raise ValueError("l'instance a retirer n'est pas une instance de type_cuisine.")
            self._cuisine_list.remove(reservations)
        except ValueError as e:
            print(e)

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
        try:
            if not isinstance(id,str):
                raise TypeError("ce n'est pas un str")
            for i in self.cuisine_list:
                if i.idCuisine == id:
                    return i
        except TypeError as e:
            print(e)
        except:
            print("erreur")

    def __str__(self):
        '''
        Renvoie une représentation textuelle de la liste de cuisine.

        PRE : -
        POST : Renvoie une chaîne de caractères contenant la liste des types de cuisine.
        '''
        return f"Liste de cuisine : {self._cuisine_list}"

    def to_json(self):
        # Convertir la liste de tables en une liste de dictionnaires JSON
        cuisine_list_json = [cuisine_list.to_json() for cuisine_list in self.cuisine_list]
        return {
            "tables": cuisine_list_json
        }

    @classmethod
    def from_json(cls, data):
        # Créer une instance de TableManager à partir d'un dictionnaire JSON
        manager = cls()
        cuisine_list = data.get("tables", [])
        for cuisine_list in cuisine_list:
            table = cuisine_list.from_json(cuisine_list)
            manager.addCuisine(table)
        return manager