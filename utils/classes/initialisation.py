from utils.classes.reservationManager import ReservationManager
from utils.classes.tableManager import TableManager
from utils.classes.typeServiceManager import TypeServiceManager
from utils.classes.type_cuisine_manager import type_cuisine_manager
import pickle
from pathlib import Path

class Initialisateur:
    """
    Cette classe sert à initialiser et gérer les différents gestionnaires (managers) pour les réservations,
    les tables, les types de service, et les types de cuisine. Elle permet également de sauvegarder 
    et de charger ces gestionnaires depuis un fichier.

    Attributs:
        fichier_sauvegarde (str): Le nom du fichier de sauvegarde.
        reservation_manager (ReservationManager): Gestionnaire des réservations.
        table_manager (TableManager): Gestionnaire des tables.
        typeServManager (TypeServiceManager): Gestionnaire des types de service.
        typeCuisineManager (type_cuisine_manager): Gestionnaire des types de cuisine.
    """
    def __init__(self):
        self.fichier_sauvegarde = 'managers.pkl'
        self.reservation_manager = None
        self.table_manager = None
        self.typeServManager = None
        self.typeCuisineManager = None

    def __str__(self):
        return f"ReservationManager avec {len(self.reservation_manager.reservations)} réservations"

    def initialiser_managers(self):
        """
        Initialise les gestionnaires avec de nouvelles instances.

        POST: 
        - Les gestionnaires de réservations, tables, types de service et types de cuisine sont initialisés.
        """
        self.reservation_manager = ReservationManager()
        self.table_manager = TableManager()
        self.typeServManager = TypeServiceManager()
        self.typeCuisineManager = type_cuisine_manager()

    def sauvegarder_managers(self):
        """
        Sauvegarde l'état actuel de tous les gestionnaires dans un fichier.

        POST: 
        - L'état actuel de l'instance Initialisateur est sauvegardé dans un fichier.
        """
        with open(self.fichier_sauvegarde, 'wb') as f:
            pickle.dump(self, f)

    def charger_ou_initialiser_managers(self):
        """
        Charge les gestionnaires à partir d'un fichier de sauvegarde, ou les initialise si le fichier n'existe pas ou est corrompu.

        POST: 
        - Si le fichier de sauvegarde existe et est valide, les gestionnaires sont chargés à partir de ce fichier.
        - Si le fichier n'existe pas ou est corrompu, les gestionnaires sont initialisés à nouveau.
        """
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

