import json
from progressbar import progressbar
from data.DataQueries import DataQueries
from apis.FantasyCalcApi import FantasyCalcApi


def refresh_fantasy_calc_projections():
    fcapi = FantasyCalcApi()
    db = DataQueries()

    db.clear_fantasy_calc_data()

    # TODO: Fantasy calc also has trade values, maybe add a table with that

    dynasty_one_qb_projections = fcapi.get_calc_rankings(True, 1, 8, 1, True)
    dynasty_two_qb_projections = fcapi.get_calc_rankings(True, 2, 8, 1, True)
    redraft_one_qb_projections = fcapi.get_calc_rankings(False, 1, 8, 1, True)
    redraft_two_qb_projections = fcapi.get_calc_rankings(False, 2, 8, 1, True)

    for player in progressbar(dynasty_one_qb_projections):
        insert_fantasy_calc_projections(db, player, True, True)

    for player in progressbar(dynasty_two_qb_projections):
        insert_fantasy_calc_projections(db, player, True, False)

    for player in progressbar(redraft_one_qb_projections):
        insert_fantasy_calc_projections(db, player, False, True)

    for player in progressbar(redraft_two_qb_projections):
        insert_fantasy_calc_projections(db, player, False, False)


def insert_fantasy_calc_projections(db, player, is_dynasty, is_one_qb):
    db.insert_fantasy_calc_data(player["player"]["sleeperId"], is_dynasty, is_one_qb,
                                player["overallRank"], player["maybeAdp"],
                                json.dumps(player).replace('\'', ''))
