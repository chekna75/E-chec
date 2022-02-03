from create_new_tournament_form import CreateNewTournamentForm
from player_manager import player_manager as pm
from tournament_manager import tournament_manager as tm
from views.choice_winner import ChoiceWinner
from views.form_update_player_rank import FormUpdatePlayerRank
from views.list_player_by_name import ListPlayerByName
from views.list_player_by_rank import ListPlayerByRank
from views.players_choice_listing import PlayersChoiceListing
from views.main_menu import MainMenu
from views.view_create_players import ViewCreatePlayers
from views.view_list_player import ViewListPlayer
from views.view_list_tournament import ViewListTournament
from views.view_retake_tournament import ViewRetakeTournament


def create_player_controller():
    form_dataP = ViewCreatePlayers().display()
    pm.create(**form_dataP, save=True)
    main_controller()


def create_tournament_controller():
    form_dataT = CreateNewTournamentForm().display()
    tm.create(**form_dataT, save=True)
    main_controller()


def list_players_controller():
    ViewListPlayer().display()
    main_controller()


def list_tournament_controller():
    ViewListTournament().display()
    main_controller()


def list_players_rank_controller():
    data = pm.find_all()
    data = sorted(data, key=lambda x: x.rank)
    ListPlayerByRank(data).display()
    main_controller()


def reprendre_tournament_controller():
    form_data = ViewRetakeTournament().display()
    tournament = tm.find_by_id(int(form_data["id"]))
    tournament.play(ChoiceWinner, pm, tm)
    tm.save_item(int(form_data["id"]))
    main_controller()


def list_player_alphabetique_controller():
    data = pm.find_all()
    data = sorted(data, key=lambda x: x.first_name)
    ListPlayerByName(data).display()
    main_controller()


def update_player_rank_controller():
    form_data = FormUpdatePlayerRank().display()
    joueur = pm.find_by_id(int(form_data["id"]))
    joueur.rank = int(form_data["rank"])
    pm.save_item(joueur.id)
    main_controller()


def main_controller():
    selection = MainMenu().display()

    if selection == 1:
        create_player_controller()

    elif selection == 2:
        create_tournament_controller()

    elif selection == 3:
        selection = PlayersChoiceListing().display()
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
