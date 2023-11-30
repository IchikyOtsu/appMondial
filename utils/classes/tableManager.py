from utils.classes.table import Table
class TableManager:
    def __init__(self):
        '''
        pre:--
        post: initialise une liste pour stocker les object
        '''
        self.tables = []

    def addTable(self,new_table):
        '''
        :param object new_table: newTable
        :add a new_table  -->liste
        pre: new_table == object
            new_table n'est pas une instance de Table
        post: ajoute des donnees dans la list de l'instance
        '''
        assert isinstance(new_table,Table), "La valeur ajouter n'est pas une instance de Table."
        self.tables.append(new_table)
    def removeTable(self,table):
        '''
        :param object table:table
        :remove a table   liste-->
         pre: entree une nouvelle instance
              table in self.tables
              table == instance de Table
        post: retrait des donnees dans la list de l'instance
        '''
        try:
            if not (isinstance(table, Table)and table in self.tables):
                raise ValueError("l'instance a retirer n'est pas une instance de Table.")
            self.tables.remove(table)
        except ValueError as e:
            print(e)
    def findTableWithNumber(self,num):
        '''
        :param int num: tableNumber
        :find a tableNumber
         pre: entre un num
            num in self.tables
            num == int
        post: retourne l'object
        '''
        try:
            if not isinstance(num, int):
                raise TypeError("La valeur donnée n'est pas un chiffre")
            for i in self.reservations:

                if i.num == num:
                    return i
        except TypeError as e :
            print(e)
        except:
            print("erreur car pas dedans")

    def afficherTables(self):
        '''
        :print:liste table
        pre:--
        post: retour chaque tables de l'instance
        '''
        for i in self.tables:
            print(i)