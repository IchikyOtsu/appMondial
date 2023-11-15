from utils.classes.reservation import Reservation
from utils.classes.reservationManager import ReservationManager
def ajouterReservation(list, managerRes):
    res = Reservation(list[0],list[1],list[2],list[3],list[4],list[5])
    managerRes.addReservation(res)
    print(managerRes)