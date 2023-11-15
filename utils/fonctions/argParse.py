import argparse


def argParse():
    parser = argparse.ArgumentParser(
        description="Entrez les détails de la réservation. out les champs d'information sont obligatoires sauf bb et pmr qui sont par défault sur non, -h (help) et -a (affiche) sont à utiliser seuls. Exemple: python main.py -nom 'John Doe' -tel 123456789 -dh '2023-10-10 19:00' -TC EU -pmr oui -bb non"
                    )

    parser.add_argument("-a", "--affichage", action="store_true", help="Affichage des réservations")
    parser.add_argument("-nom", type=str, help="Nom du client. Exemple: 'John Doe'")
    parser.add_argument("-tel", type=int, help="Numéro de téléphone. Exemple: 123456789")
    parser.add_argument("-dh", type=str,
                        help="Date et heure de la réservation (format AAAA-MM-JJ HH:MM). Exemple: '2023-10-10 19:00' Vous devez mettre cette date entre '' ou guillemet. ")
    parser.add_argument("-TC", type=str, help="ID du type de cuisine. Choix : Europe(eu), Asie (asi), Amérique du Nord/Sud (as/an), Afrique (af). Veuillez entrer l'id et non le nom complet.")
    parser.add_argument("-pmr", type=lambda x: (str(x).lower() == 'true'),
                        help="Besoin PMR Choix: (Oui/Nom)")
    parser.add_argument("-bb", type=lambda x: (str(x).lower() == 'true'),
                        help="Chaise bébé nécessaire Choix: (oui/non)")


    args = parser.parse_args()
    if args.affichage:
        return False
    else:
        return [args.nom,args.tel,args.dh,args.TC, args.pmr, args.bb]
