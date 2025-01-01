import json
from progressbar import progressbar
from apis.DynastyDaddyApi import DynastyDaddyApi, FantasyMarket
from data.DataQueries import DataQueries


def refresh_dynasty_daddy_projections():
    ddapi = DynastyDaddyApi()
    db = DataQueries()

    db.clear_dynasty_daddy_data()
    db.clear_dd_player_data()


    player_data = ddapi.get_player_data()
    for player in progressbar(player_data):
        insert_dynasty_daddy_player_data(db, player)

    for market in progressbar(FantasyMarket.__members__.values()):
        projections = ddapi.get_projections_data(market)

        for player in projections:
            insert_dynasty_daddy_projections(db, player, market.name)


def insert_dynasty_daddy_player_data(db, player):
    db.insert_dynasty_daddy_player_data(player['name_id'], player['sleeper_id'], player['first_name'].replace('\'', ''),
                                        player['last_name'].replace('\'', ''), player['position'], json.dumps(player).replace('\'', ''))

def insert_dynasty_daddy_projections(db: DataQueries, player, market):
    db.insert_dynasty_daddy_data(player['name_id'], market, player['overall_rank'],
                                 player['sf_overall_rank'], json.dumps(player))