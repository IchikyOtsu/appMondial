from utils.classes.reservation import Reservation
from utils.classes.reservationManager import ReservationManager
from utils.classes.tableManager import TableManager
from utils.classes.table import Table
from utils.classes.typeServiceManager import TypeServiceManager
from utils.classes.typeService import TypeService
from utils.fonctions.initial import initial
from utils.fonctions.ajoutRes import ajouterReservation
from utils.fonctions.argParse import argParse
from utils.classes.type_cuisine_manager import type_cuisine_manager
from utils.classes.type_cuisine import type_cuisine
from utils.fonctions.attrib import attribution
from utils.fonctions.verifRes import verifRes
from utils.fonctions.supprimerRes import supprimerRes
def main():
    '''
        liste = ['nom',475309844,5,'2023',1,False,True]
        ajouterReservation(liste,managerRes)
        managerRes.affichage()
        # Après modifications des managers
        init.sauvegarder_managers()
    '''
    init = initial()
    # Utilisation des managers
    managerRes = init.reservation_manager
    managerTable = init.table_manager
    managerService = init.typeServManager
    managerCuisine = init.typeCuisineManager

    liste = argParse(managerRes)
    
    if liste is False:
        managerRes.affichage()
        return 0
    else:
        if liste[0] is False:
            managerRes.affichage()
            managerRes = liste[1]
            init.sauvegarder_managers()
            return 0
    if None in liste:
        print('python main.py -h')
        return 0

    # python .\main.py -nom Brice -tel 0471371916 -dh "2023-11-15 14:30" -nbr 4 -TC eu -pmr non -bb non
    liste = verifRes(liste,managerCuisine)
    #print(liste)
    if liste is False:
        return 0

    liste = attribution(liste,managerRes,managerTable,managerCuisine)
    if liste is False:
        print("Désolé, il n'y a plus de place !")
        return 1
    #print(liste)
    ajouterReservation(liste,managerRes)

    init.sauvegarder_managers()

def dataBase():
    init = initial()

    # Utilisation des managers
    managerRes = init.reservation_manager
    managerTable = init.table_manager
    managerService = init.typeServManager
    managerCuisine = init.typeCuisineManager

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
    eu= type_cuisine('eu','Europe','S1')
    azi = type_cuisine('azi', 'Asie', 'S1')
    ads = type_cuisine('as', 'Amérique du Sud', 'S1')
    adn = type_cuisine('an', 'Amérique du Nord', 'S1')
    afri = type_cuisine('af', 'Afrique', 'S1')
    vip = type_cuisine('vip', 'VIP', 'S2')
    managerCuisine.addCuisine(eu,azi,ads,adn,afri,vip)
    managerCuisine.displayList()

    init.sauvegarder_managers()

def afficherManager():
    init = initial()

    # Utilisation des managers
    managerRes = init.reservation_manager
    managerTable = init.table_manager
    managerService = init.typeServManager
    managerCuisine = init.typeCuisineManager

    managerService.afficherServices()
    managerCuisine.displayList()
    managerTable.afficherTables()
if __name__ == '__main__':
    main()