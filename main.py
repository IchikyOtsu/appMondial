from utils.classes.reservation import Reservation
from utils.classes.reservationManager import ReservationManager
from utils.classes.tableManager import TableManager
from utils.classes.table import Table
from utils.classes.typeServiceManager import TypeServiceManager
from utils.classes.typeService import TypeService
from utils.fonctions.initial import initial
from utils.fonctions.ajoutRes import ajouterReservation
from utils.fonctions.argParse import argParse
def main():

    init = initial()

    # Utilisation des managers
    managerRes = init.reservation_manager
    managerTable = init.table_manager
    managerService = init.typeServManager
    '''
    liste = ['nom',475309844,5,'2023',1,False,True]
    ajouterReservation(liste,managerRes)
    managerRes.affichage()
    # Après modifications des managers
    init.sauvegarder_managers()
    '''

    liste = argParse()
    if liste == False:
        managerRes.affichage()
        return 0

    print(liste)

def dataBase():
    init = initial()

    # Utilisation des managers
    managerRes = init.reservation_manager
    managerTable = init.table_manager
    managerService = init.typeServManager
    serv1= TypeService('S1','Basique','RDC')
    serv2 = TypeService('S2', 'VIP', 'RT')
    managerService.addService(serv2)
    managerService.addService(serv1)
    managerService.afficherServices()


    for i in range(26):
        table = Table(i+1, 4,'S1')
        managerTable.addTable(table)
    table15 = Table(27, 15, 'S1')
    managerTable.addTable(table15)
    for i in range(4):
        tableVip = Table(i+28,4,'S2')
        managerTable.addTable(tableVip)

    managerTable.afficherTables()


if __name__ == '__main__':
    main()
