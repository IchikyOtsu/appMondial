class TableManager:
    def __init__(self):
        self.tables = []

    def addTable(self,new_table):
        '''
        :param object new_table: newTable
        :add a new_table  -->liste
        '''
        self.tables.append(new_table)
    def removeTable(self,table):
        '''
        :param object table:table
        :remove a table   liste-->
        '''
        self.tables.remove(table)
    def findTableWithNumber(self,num):
        '''
        :param int num: tableNumber
        :find a tableNumber
        '''
        for i in self.tables:
            if i.numTable == num:
                return i
    def afficherTables(self):
        '''
        :print:liste table
        '''
        for i in self.tables:
            print(i)
