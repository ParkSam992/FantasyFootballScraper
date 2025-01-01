import json
from apis.SleeperApi import SleeperApi
from data.DataQueries import DataQueries
from progressbar import progressbar

def refresh_sleeper_projections():
    sleeper_api = SleeperApi()
    db = DataQueries()

    print("Clearing current data")
    db.clear_sleeper_data()

    print("Getting projections data")
    projections = sleeper_api.get_projections_data(2025)
    print("Writing projections data")
    for player in progressbar(projections):
        db.insert_sleeper_data(player['player_id'], player['player']['first_name'].replace('\'', ''),
                               player['player']['last_name'].replace('\'', ''), player['player']['position'],
                               player['stats'], json.dumps(player).replace('\'', ''))




