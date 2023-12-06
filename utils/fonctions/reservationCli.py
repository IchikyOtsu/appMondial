from datetime import datetime
from prompt_toolkit.shortcuts import radiolist_dialog, input_dialog
from tabulate import tabulate
import questionary

def select_date():
    """Fonction qui permet de réserver une table"""
    result = input_dialog(
        title="Sélectionnez une date",
        text="Entrez la date au format YYYY-MM-DD:",
        default=str(datetime.now().date())
    ).run()

    try:
        # Vérifie si la date est au format valide
        selected_date = datetime.strptime(result, "%Y-%m-%d").date()
        return selected_date.strftime("%Y-%m-%d")
    except ValueError:
        print("Format de date invalide. Veuillez utiliser le format YYYY-MM-DD.")
        return select_date()

def reservationCli():
    """Fonction qui permet de réserver une table"""
    nom = input("Entrez le nom : ")
    tel = input("Entrez le numéro de téléphone : ")
    date = select_date()
    # Générer une liste de toutes les heures de la journée
    heures = [f"{h:02d}:{m:02d}" for h in range(24) for m in range(0, 60, 15)]

    heure = questionary.select("Sélectionnez une heure :", choices=heures).ask()

    date_heure = date + " " + heure

    nbr_personne = int(input("Entrez le nombre de personnes : "))

    type_nourriture = questionary.select(
        "Sélectionnez le type de nourriture :",
        choices=["Europe", "Asie", "Amérique du Nord", "Amérique du Sud", "Afrique", "VIP"]
    ).ask()

    pmr = questionary.select('Besoin PMR ?', choices=['Oui', 'Non']).ask()

    chaise_bebe = questionary.select('Besoin d\'une chaise bébé ?', choices=['Oui', 'Non']).ask()

    # Récapitulatif des informations saisies
    recap_table = [
        ["Nom", nom],
        ["Téléphone", tel],
        ["Date", date],
        ["Heure", heure],
        ["Nombre de personnes", nbr_personne],
        ["Type de nourriture", type_nourriture],
        ["PMR", pmr],
        ["Chaise bébé", chaise_bebe],
    ]
    switcher = {
        "Europe": "eu",
        "Asie": "azi",
        "Amérique du Nord": "an",
        "Amérique du Sud": "as",
        "Afrique": "af",
        "VIP": "vip"
    }

    type_nourriture = switcher.get(type_nourriture, "Invalid choice")

    # Affichage du tableau récapitulatif
    print("\nRécapitulatif des informations saisies:")
    print(tabulate(recap_table, tablefmt="fancy_grid"))
    return[nom, tel, date_heure, type_nourriture, pmr, chaise_bebe, nbr_personne,]