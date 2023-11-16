from utils.classes.reservationManager import ReservationManager
from utils.classes.tableManager import TableManager
from utils.classes.type_cuisine_manager import type_cuisine_manager

def attribution(list, managerRes, managerTable, managerCuisine):
    nomClient, numTel, dateHeure, idTypeCuisine, pmr, bb,nbr = list
    cuisine = managerCuisine.findCuisineByid(idTypeCuisine)
    typeServ = cuisine.idService
    for table in managerTable.tables:
        if table.capaciteTable >= nbr and table.idService == typeServ:
            listeRes = managerRes.findReservationByTable(table.numTable)
            table_disponible = True
            for res in listeRes:
                if res.dateHeure == dateHeure:
                    table_disponible = False
                    break
            if table_disponible:
                list.append(table.numTable)
                return list
    return False
