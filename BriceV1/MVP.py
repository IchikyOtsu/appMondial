import re
from datetime import datetime
import pickle

def sauvegarder_reservations(reservations):
    with open('reservations.pkl', 'wb') as fichier:
        pickle.dump(reservations, fichier)
def charger_reservations():
    try:
        with open('reservations.pkl', 'rb') as fichier:
            reservations = pickle.load(fichier)
            return [r for r in reservations if datetime.strptime(r.date_heure, '%Y-%m-%d %H:%M') > datetime.now()]
    except FileNotFoundError:
        return []


class Reservation:
    def __init__(self, nom, numero_client, type_service, date_heure, nb_personnes, pmr, bebes):
        self.nom = nom
        self.numero_client = numero_client
        self.type_service = type_service
        self.date_heure = date_heure
        self.nb_personnes = nb_personnes
        self.pmr = pmr
        self.bebes = bebes

class GestionnaireReservations:
    def __init__(self):
        self.reservations = []

    def ajouter_reservation(self, reservation):
        self.reservations.append(reservation)
        print("Réservation ajoutée avec succès.")

    def afficher_reservations(self):
        if not self.reservations:
            print("Aucune réservation existante.")
        else:
            reservations = [r for r in self.reservations if datetime.strptime(r.date_heure, '%Y-%m-%d %H:%M') > datetime.now()]
            reservations.sort(key=lambda r: r.date_heure)
            for i, reservation in enumerate(reservations, 1):
                print(f"Réservation {i}:")
                self.afficher_reservation(reservation)

    @staticmethod
    def afficher_reservation(reservation):
        print(f"Nom du client: {reservation.nom}")
        print(f"Numéro du client: {reservation.numero_client}")
        print(f"Type de service: {reservation.type_service}")
        print(f"Date et heure de réservation: {reservation.date_heure}")
        print(f"Nombre de personnes attendues: {reservation.nb_personnes}")
        print(f"Besoin d'assistance pour les PMR: {reservation.pmr}")
        print(f"Présence de bébés: {reservation.bebes}")
        print("\n")

def saisir_type_service():
    services_disponibles = ['Europe', 'Afrique', 'Amérique du Nord', 'Amérique du Sud', 'Asie']
    while True:
        type_service = input("Type de service demandé (Europe/Afrique/Amérique du Nord/Amérique du Sud/Asie) : ").capitalize()
        if type_service in services_disponibles:
            return type_service
        else:
            print("Choix non valide. Veuillez choisir parmi les options disponibles.")

def saisir_oui_ou_non(message):
    while True:
        reponse = input(message).strip().lower()
        if reponse in ['oui', 'non']:
            return reponse
        else:
            print("Répondez par 'Oui' ou 'Non'.")

def saisir_date_future():
    while True:
        date_heure = input("Date et heure de réservation (YYYY-MM-DD HH:MM) : ")
        try:
            reservation_date = datetime.strptime(date_heure, '%Y-%m-%d %H:%M')
            now = datetime.now()
            if reservation_date > now:
                return date_heure
            else:
                print("La date de réservation doit être dans le futur.")
        except ValueError:
            print("Le format de la date n'est pas valide.")

def saisir_reservation():
    nom = input("Nom du client : ")
    numero_client = input("Numéro du client : ")
    type_service = saisir_type_service()
    date_heure = saisir_date_future()
    nb_personnes = input("Nombre de personnes attendues : ")
    pmr = saisir_oui_ou_non("Besoin d'assistance pour les PMR (Oui/Non) : ")
    bebes = saisir_oui_ou_non("Présence de bébés (Oui/Non) : ")

    return Reservation(nom, numero_client, type_service, date_heure, nb_personnes, pmr, bebes)

def main():
    gestionnaire_reservations = GestionnaireReservations()
    gestionnaire_reservations.reservations = charger_reservations()
    while True:
        print("Menu:")
        print("1. Réserver une table")
        print("2. Afficher les réservations")
        print("3. Quitter")

        choice = input("Choisissez une option (1/2/3): ")

        if choice == "1":
            reservation = saisir_reservation()
            try:
                gestionnaire_reservations.ajouter_reservation(reservation)

            except ValueError as e:
                print(f"Erreur : {e}")

        elif choice == "2":
            gestionnaire_reservations.afficher_reservations()
        elif choice == "3":
            sauvegarder_reservations(gestionnaire_reservations.reservations)
            break
        else:
            print("Choix non valide. Veuillez choisir parmi les options disponibles.")

if __name__ == "__main__":
    main()
