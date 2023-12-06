from utils.classes.reservation import Reservation
from utils.classes.reservationManager import ReservationManager
def ajouterReservation(list, managerRes):
    id = 1
    for reserv in managerRes.reservations:
        if reserv.idRes == id:
            id+=1
            continue
        else:
            break
    res = Reservation(list[0],list[1],list[7],list[2],list[3],list[4],list[5],list[6],id)
    managerRes.addReservation(res)
    print(f'La réservation a bien été ajoutée !')
    print(res)
