import json
from apis.SleeperApi import SleeperApi
from data.DataQueries import DataQueries

def refresh_sleeper_projections():
    sleeper_api = SleeperApi()
    db = DataQueries()

    print("Clearing current data")
    db.clear_sleeper_data()

    print("Getting new data")
    projections = sleeper_api.get_projections_data(2025)
    print("Writing new data")
    for player in projections:
        db.insert_sleeper_data(player['player_id'], player['player']['first_name'].replace('\'', ''),
                               player['player']['last_name'].replace('\'', ''), player['player']['position'],
                               player['stats'], json.dumps(player).replace('\'', ''))


