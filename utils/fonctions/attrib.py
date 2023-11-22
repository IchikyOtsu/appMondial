from utils.classes.reservationManager import ReservationManager
from utils.classes.tableManager import TableManager
from utils.classes.type_cuisine_manager import type_cuisine_manager

def attribution(list, managerRes, managerTable, managerCuisine):
    """
    Attribue une table à une réservation en fonction de la capacité requise, du type de cuisine, et de la disponibilité.

    PRE: 
    - list: Une liste contenant les détails de la réservation. Elle doit contenir le nom du client, 
      le numéro de téléphone, la date et l'heure, l'ID du type de cuisine, les besoins en accessibilité PMR,
      les besoins en chaise bébé et le nombre de personnes.
    - managerRes: Une instance de ReservationManager pour gérer les réservations.
    - managerTable: Une instance de TableManager pour gérer les informations des tables.
    - managerCuisine: Une instance de type_cuisine_manager pour gérer les types de cuisine.

    POST: 
    - Renvoie la liste originale avec le numéro de la table attribuée ajouté à la fin si une table disponible est trouvée.
    - Renvoie False si aucune table correspondante n'est disponible.
    
    La fonction vérifie chaque table pour s'assurer qu'elle correspond aux critères requis (capacité, type de service)
    et qu'elle est disponible à la date et l'heure demandées. Si une table correspondante est trouvée,
    le numéro de cette table est ajouté à la liste de réservation et la liste mise à jour est renvoyée.
    """
    
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
