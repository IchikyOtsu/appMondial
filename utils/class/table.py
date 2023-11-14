class Reservation:
    def __init__(self, table_number, client_name, phone_number, date_time, cuisine_id, pmr, baby):
        self.table_number = table_number
        self.client_name = client_name
        self.phone_number = phone_number
        self.date_time = date_time
        self.cuisine_id = cuisine_id
        self.pmr = pmr
        self.baby = baby

    def __str__(self):
        return f"Reservation for {self.client_name} at table {self.table_number} on {self.date_time}."

# Classe pour gérer plusieurs réservations
class ReservationManager:
    def __init__(self):
        self.reservations = []

    def add_reservation(self, reservation):
        self.reservations.append(reservation)

    def remove_reservation(self, reservation):
        self.reservations.remove(reservation)

    def find_reservation_by_name(self, client_name):
        return [res for res in self.reservations if res.client_name == client_name]

    def list_reservations(self):
        for reservation in self.reservations:
            print(reservation)

# Exemple d'utilisation
manager = ReservationManager()
res1 = Reservation(1, "John Doe", "123456789", "2023-11-15 19:00", "Asian", False, True)
res2 = Reservation(2, "Jane Smith", "987654321", "2023-11-16 20:00", "European", True, False)

manager.add_reservation(res1)
manager.add_reservation(res2)

manager.list_reservations()
