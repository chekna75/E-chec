
from create_new_tournament_form import CreateNewTournamentForm
from player_manager import player_manager as pm
from tournament_manager import tournament_manager as tm
from table import Table
from view import ChoiceWinner, Menu
from form import Form


def create_player_controller():
    form_dataP = Form(title="Crée un joueur", fields=[("first_name", "prénom"),
                                                      ("last_name", "nom"),
                                                      ("birthdate", "date de naissance(AAAA-MM-JJ)"),
                                                      ("gender", "genre"),
                                                      ("rank", "rang")]).display()
    pm.create(**form_dataP, save=True)
    main_controller()


def create_tournament_controller():
    form_dataT = CreateNewTournamentForm().display()
    tm.create(**form_dataT, save=True)
    main_controller()


def list_players_controller():
    Table(title="Liste des joueurs", items=pm.find_all()).display()
    main_controller()


def list_tournament_controller():
    Table(title="Liste des tournois", items=tm.find_all()).display()
    main_controller()


def list_players_rank_controller():
    # sorted() pour trier
    data = pm.find_all()
    data = sorted(data, key=lambda x: x.rank)
    Table(title="Liste des joueur par classement", items=data).display()
    main_controller()


def reprendre_tournament_controller():
    form_data = Form(title="Reprendre un tournoi", fields=
                     [("id","id du tournoi", str)]).display()
    tournament = tm.find_by_id(int(form_data["id"]))
    tournament.play(ChoiceWinner, tm)
    print(form_data)
    tm.save_item(int(form_data["id"]))
    # main_controller()


def list_player_alphabetique_controller():
    data = pm.find_all()
    data = sorted(data, key=lambda x: x.first_name)
    Table(title="Liste des joueur par odre alphabetique", items=data).display()
    main_controller()

def update_player_rank_controller():
    form_data = Form(title="Modifier rang", fields=
                     [("id","id du joueur"), ("rank", "Nouveau classement")]).display()
    joueur = pm.find_by_id(int(form_data["id"]))
    joueur.rank = int(form_data["rank"])
    pm.save_item(joueur.id)
    main_controller()


def main_controller():

    selection = Menu(title="Menu principal", choices=["Creer un joueur",
                                                      " Creer un tournois",
                                                      " Liste des joueur",
                                                      " Lister un tournois",
                                                      " Liste des joueur par classement",
                                                      " Afficher les rapport",
                                                      " Modifier un joueur",
                                                      " Reprendre un tournois"]).display()

    if selection == 1:
        create_player_controller()

    elif selection == 2:
        create_tournament_controller()

    elif selection == 3:
        selection = Menu(title="Liste des joueurs", choices=["Liste des joueurs",
                                                             " Liste des joueurs par classement",
                                                             " Liste des joueurs par ordre alphabetique"]).display()
        if selection == 1:
            list_players_controller()

        elif selection == 2:
            list_players_rank_controller()

        elif selection == 3:
            list_player_alphabetique_controller()

    elif selection == 4:
        list_tournament_controller()

    elif selection == 5:
        list_players_rank_controller()

    elif selection == 6:
        list_player_alphabetique_controller()

    elif selection == 7:
        update_player_rank_controller()

    elif selection == 8:
        reprendre_tournament_controller()
    else:
        print("Erreur")


if __name__ == "__main__":
    main_controller()
