class Table:
    '''
    class used for init a new table
    '''
    def __init__(self,numTable,capaciteTable,idService):
        self.__numTable = int(numTable)
        self.__capaciteTable = int(capaciteTable)
        self.__idService = idService

    def __str__(self):
        return f"numTable: {self.__numTable}, capaciteTable: {self.__capaciteTable}, idService: {self.__idService} "

    '''
    :rest: modify and security
    '''
    @property
    def numTable(self):
        return self.__numTable
    @numTable.setter
    def numTable(self, new_numTable):
        self.__numTable = new_numTable

    @property
    def capaciteTable(self):
        return self.__capaciteTable
    @capaciteTable.setter
    def capaciteTable(self, new_capaciteTable):
        self.__capaciteTable = new_capaciteTable

    @property
    def idService(self):
        return self.__idService
    @idService.setter
    def idService(self, new_idService):
        self.__idService = new_idService
