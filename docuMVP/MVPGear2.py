from datetime import datetime, timedelta
import pickle
import argparse

liste_reservations = {}


def sauvegarder_reservations(liste):
    with open('reservations.pkl', 'wb') as fichier:
        pickle.dump(liste, fichier)


def charger_reservations():
    global liste_reservations
    try:
        with open('reservations.pkl', 'rb') as fichier:
            liste_reservations = pickle.load(fichier)
    except (FileNotFoundError, EOFError):
        liste_reservations = {}
    return liste_reservations


class Reservation:
    def __init__(self, nom, numero_client, type_service, date_heure, nb_personnes, numTable, pmr, bebes):
        self.nom = nom
        self.numero_client = numero_client
        self.type_service = type_service
        self.date_heure = date_heure
        self.nb_personnes = nb_personnes
        self.numTable = numTable
        self.pmr = pmr
        self.bebes = bebes

    def date_passee(self):
        now = datetime.now()
        date_heure_obj = datetime.strptime(self.date_heure, '%Y-%m-%d %H:%M')
        return date_heure_obj < now

    def conflit_horaire(self, autre_reservation):
        delta = timedelta(hours=2)

        debut_autre = datetime.strptime(autre_reservation.date_heure, '%Y-%m-%d %H:%M') - delta
        fin_autre = datetime.strptime(autre_reservation.date_heure, '%Y-%m-%d %H:%M') + delta

        debut_nouveau = datetime.strptime(self.date_heure, '%Y-%m-%d %H:%M') - delta
        fin_nouveau = datetime.strptime(self.date_heure, '%Y-%m-%d %H:%M') + delta

        return not (fin_nouveau < fin_autre or debut_nouveau > debut_autre)



    def __str__(self):
        return f"Reservation au nom de {self.nom} à {self.date_heure} du type {self.type_service}, avec {self.nb_personnes} personne(s) dont {self.pmr} personne(s) à mobilité réduite et {self.bebes} bébé(s)"


def valider_infos(type_service, date_heure, nb_personnes, num_table, pmr, bebes):
    services_valides = ['Europe', 'Afrique', 'Amérique du Nord', 'Amérique du Sud', 'Asie']
    if type_service not in services_valides:
        print("Erreur: Le type de service doit être l'un des suivants:", services_valides)
        return False
    try:
        datetime.strptime(date_heure, '%Y-%m-%d %H:%M')
    except ValueError:
        print("Erreur: Format de date et d'heure invalide. Utilisez 'YYYY-MM-DD HH:MM'")
        return False
    if not (nb_personnes.isdigit() and num_table.isdigit()):
        print("Erreur: Le nombre de personnes et le numéro de table doivent être des nombres valides.")
        return False
    if pmr not in ['Oui', 'Non'] or bebes not in ['Oui', 'Non']:
        print("Erreur: Les valeurs pour pmr et bebes doivent être 'Oui' ou 'Non'.")
        return False
    return True


def ajouterReservation(nom, numero_client, type_service, date_heure, nb_personnes, pmr, bebes,numTable):
    print(liste_reservations)
    if None in (nom, numero_client, type_service, date_heure, nb_personnes, numTable):
        print("Erreur: Tous les champs doivent être renseignés.")
        return liste_reservations

    bebes = "Non" if bebes is None or not bebes else "Oui"
    pmr = "Non" if pmr is None or not pmr else "Oui"

    if not valider_infos(type_service, date_heure, nb_personnes, numTable, pmr, bebes):
        return liste_reservations

    reservation = Reservation(nom, numero_client, type_service, date_heure, nb_personnes, numTable, pmr, bebes)

    if reservation.date_passee():
        print("Erreur: La date de réservation est passée.")
        return liste_reservations

    if reservation.numTable not in liste_reservations:
        liste_reservations[reservation.numTable] = []

    for resa in liste_reservations[reservation.numTable]:
        if reservation.conflit_horaire(resa):
            print(f"ATTENTION: La table {reservation.numTable} est déjà réservée dans cette plage horaire.")
            return liste_reservations
    liste_reservations[reservation.numTable].append(reservation)

    sauvegarder_reservations(liste_reservations)

    return liste_reservations

def afficheReservations():
    for num_table, reservations in liste_reservations.items():
        for reservation in reservations:
            print(reservation)

def main():
    charger_reservations()
    parser = argparse.ArgumentParser(prog="Reservation", description="Prends les reservations pour le restaurant")
    parser.add_argument("-n", "--nom", help="Nom pour la réservation")
    parser.add_argument("-num", "--numero", help="Numéro de client")
    parser.add_argument("-t", "--type", help="Type de service")
    parser.add_argument("-d", "--date", help="Date et heure de la réservation (format: 'YYYY-MM-DD HH:MM')")
    parser.add_argument("-nbr", "--nombreClient", help="Nombre de clients")
    parser.add_argument("-pmr", "--PMR", action="store_true", help="Nombre de personnes à mobilité réduite")
    parser.add_argument("-bb", "--bébé", action="store_true", help="Nombre de bébés")
    parser.add_argument("-tb", "--numTable", help="Numéro de table")
    parser.add_argument("-a", "--affichage", action="store_true", help="Affichage des réservations")

    args = parser.parse_args()
    if args.affichage:
        afficheReservations()
    else:
        ajouterReservation(args.nom, args.numero, args.type, args.date, args.nombreClient, args.PMR, args.bébé, args.numTable)


if __name__ == "__main__":
    main()
