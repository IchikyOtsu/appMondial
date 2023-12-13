from utils.classes.table import Table
class TableManager:
    def __init__(self):
        '''
        Initialise un gestionnaire de tables avec une liste vide de tables.

        PRE : -
        POST : Crée une liste vide pour stocker les tables.
        '''
        self.tables = []

    def addTable(self, new_table):
        '''
        Ajoute une nouvelle table à la liste des tables.

        PRE : new_table doit être un objet de type Table.
        POST : Ajoute la nouvelle table à la liste des tables.
        '''
        assert isinstance(new_table,Table), "La valeur ajouter n'est pas une instance de Table."
        self.tables.append(new_table)

    def removeTable(self, table):
        '''
        Supprime une table de la liste des tables.

        PRE : table 
        POST : Supprime la table spécifiée de la liste des tables.

        Raise : table doit être une table existante dans la liste et une instance de table.
        '''

        if not isinstance(table, Table) :
            raise ValueError("l'instance a retirer n'est pas une instance de Table.")
        if not table in self.tables:
            raise ValueError("l'instance a retirer n'est pas dans la liste des tables.")
        self.tables.remove(table)

    def findTableWithNumber(self, num):
        '''
        Recherche une table avec un numéro spécifique.

        PRE : num 
        POST : Renvoie la table correspondant au numéro spécifié s'il en existe une.

        Raise : num doit être un entier correspondant au numéro de table à rechercher.
        '''
        if not isinstance(num, int):
                raise TypeError("La valeur donnée n'est pas un chiffre")
        for i in self.reservations:
            if i.num == num:
                return i
        return None
    
    def afficherTables(self):
        '''
        Affiche les informations sur les tables.

        PRE : -
        POST : Affiche les informations de chaque table dans la liste.
        '''
        for i in self.tables:
            print(i)
    
    def to_json(self):
        # Convertir la liste de tables en une liste de dictionnaires JSON
        tables_json = [table.to_json() for table in self.tables]
        return {
            "tables": tables_json
        }

    @classmethod
    def from_json(cls, data):
        # Créer une instance de TableManager à partir d'un dictionnaire JSON
        manager = cls()
        tables_data = data.get("tables", [])
        for table_data in tables_data:
            table = Table.from_json(table_data)
            manager.addTable(table)
        return manager
