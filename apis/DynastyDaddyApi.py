import requests
from enum import Enum

class FantasyMarket(Enum):
    # on 12/30/24 those commented out contain lots of outlier data I don't want included
    # should look at the data again when ADP's are actually up to date
    ADP_DADDY_DYN = 6
    KEEP_TRADE_CUT_DYN = 0
    DYNASTY_PROCESS_DYN = 2
    FANTASY_NAVIGATOR_DYN = 3
    # PRO_FOOTBALL_NETWORK_DYN = 9
    # DRAFT_SHARKS_DYN = 12
    ADP_DADDY_STD = 7
    KEEP_TRADE_CUT_STD = 4
    FANTASY_NAVIGATOR_STD = 8
    # PRO_FOOTBALL_NETWORK_STD = 10
    # DRAFT_SHARKS_STD = 13

class DynastyDaddyApi:
    def __init__(self):
        self.base_url = 'https://dynasty-daddy.com'

    def get_projections_data(self, market: FantasyMarket):
        endpoint = f'/api/v1/player/all/market/{market.value}'
        full_url = self.base_url + endpoint
        response = requests.get(full_url)
        return response.json()

    def get_player_data(self):
        endpoint = f'/api/v1/player/all/today'
        full_url = self.base_url + endpoint
        response = requests.get(full_url)
        return response.json()