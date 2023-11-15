from utils.classes.reservationManager import ReservationManager
from utils.classes.tableManager import TableManager
from utils.classes.typeServiceManager import TypeServiceManager
from utils.classes.type_cuisine_manager import type_cuisine_manager
import pickle
from pathlib import Path

class Initialisateur:
    def __init__(self):
        self.fichier_sauvegarde = 'managers.pkl'
        self.reservation_manager = None
        self.table_manager = None
        self.typeServManager = None
        self.typeCuisineManager = None
    
    def __str__(self):
        return f"ReservationManager avec {len(self.reservation_manager.reservations)} réservations"

    def initialiser_managers(self):
        self.reservation_manager = ReservationManager()
        self.table_manager = TableManager()
        self.typeServManager = TypeServiceManager()
        self.typeCuisineManager = type_cuisine_manager()

    def sauvegarder_managers(self):
        with open(self.fichier_sauvegarde, 'wb') as f:
            pickle.dump(self, f)

    def charger_ou_initialiser_managers(self):
        try:
            if Path(self.fichier_sauvegarde).exists():
                with open(self.fichier_sauvegarde, 'rb') as f:
                    loaded_init = pickle.load(f)
                    self.reservation_manager = loaded_init.reservation_manager
                    self.table_manager = loaded_init.table_manager
                    self.typeServManager = loaded_init.typeServManager
                    self.typeCuisineManager = loaded_init.typeCuisineManager
            else:
                self.initialiser_managers()
        except (EOFError, pickle.UnpicklingError):
            self.initialiser_managers()

