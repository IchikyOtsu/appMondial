from utils.classes.reservation import Reservation

class ReservationManager:
    def __init__(self):
        """
        Pre: --
        Post: Initialisation de l'instance avec une liste vide de réservations.
        """
        self.reservations = []

    def add_reservation(self, new_reservation):
        """
        Ajoute une nouvelle réservation à la liste.

        Pre: new_reservation doit être une instance de Reservation.
        Post: new_reservation est ajoutée à la liste des réservations.

        :param Reservation new_reservation: La nouvelle réservation à ajouter.
        """
        assert isinstance(new_reservation, Reservation), "Ce n'est pas une instance de Reservation"
        self.reservations.append(new_reservation)

    def remove_reservation(self, reservation_to_remove):
        """
        Supprime une réservation de la liste.

        Pre: reservation_to_remove doit être une instance de Reservation et faire partie de self.reservations.
        Post: reservation_to_remove est retirée de la liste des réservations.

        :param Reservation reservation_to_remove: La réservation à supprimer.
        """
        try:
            if not (isinstance(reservation_to_remove, Reservation) and reservation_to_remove in self.reservations):
                raise TypeError("L'élément à supprimer doit être une instance de Reservation présente dans la liste.")
            self.reservations.remove(reservation_to_remove)
        except TypeError as e:
            print(e)

    def find_reservation_by_name(self, name):
        """
        Trouve une réservation par son nom.

        Pre: name doit être une chaîne de caractères.
        Post: Retourne l'objet Reservation correspondant si trouvé, sinon None.

        :param str name: Le nom de la réservation à trouver.
        :return: L'objet Reservation correspondant, ou None si non trouvé.
        """
        try:
            if not isinstance(name, str):
                raise TypeError("La valeur donnée n'est pas une chaîne de caractères.")
            for reservation in self.reservations:
                if reservation.nom == name:
                    return reservation
        except TypeError as e:
            print(e)

    def find_reservation_by_table(self, table):
        """
        Trouve les réservations pour une table spécifique.

        Pre: table doit être un entier.
        Post: Retourne une liste des réservations pour cette table.

        :param int table: Le numéro de la table.
        :return: Liste des réservations pour cette table.
        """
        try:
            if not isinstance(table, int):
                raise TypeError("La valeur donnée n'est pas un entier.")
            reservations_for_table = []
            for reservation in self.reservations:
                if reservation.num_table == table:
                    reservations_for_table.append(reservation)

            return reservations_for_table
        except TypeError as e:
            print(e)

    def display_reservations(self):
        """
        Affiche toutes les réservations.

        Pre: --
        Post: Affiche chaque réservation de la liste.
        """
        for reservation in self.reservations:
            print(reservation)
