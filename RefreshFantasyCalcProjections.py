import json
from progressbar import progressbar
from data.DataQueries import DataQueries
from apis.FantasyCalcApi import FantasyCalcApi


def refresh_fantasy_calc_projections():
    fcapi = FantasyCalcApi()
    db = DataQueries()

    db.clear_fantasy_calc_data()

    dynasty_one_qb_projections = fcapi.get_calc_rankings(True, 1, 8, 1, True)
    dynasty_two_qb_projections = fcapi.get_calc_rankings(True, 2, 8, 1, True)
    redraft_one_qb_projections = fcapi.get_calc_rankings(False, 1, 8, 1, True)
    redraft_two_qb_projections = fcapi.get_calc_rankings(False, 2, 8, 1, True)

    for dynasty_player in progressbar(dynasty_one_qb_projections):
        dynasty_sf_player = next((p for p in dynasty_two_qb_projections if p["player"]["sleeperId"] == dynasty_player["player"]["sleeperId"]), None)
        insert_fantasy_calc_projections(db, dynasty_player, dynasty_sf_player, True)

    for player in progressbar(redraft_one_qb_projections):
        sf_player = next((p for p in redraft_two_qb_projections if p["player"]["sleeperId"] == player["player"]["sleeperId"]), None)
        insert_fantasy_calc_projections(db, player, sf_player, False)



def insert_fantasy_calc_projections(db, player, sf_player, is_dynasty):
    db.insert_fantasy_calc_data(player["player"]["sleeperId"], is_dynasty,
                                player["overallRank"], player["maybeAdp"],
                                sf_player["overallRank"], sf_player["maybeAdp"],
                                json.dumps(player).replace('\'', ''))
