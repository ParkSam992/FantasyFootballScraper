import requests

class FantasyCalcApi:
    def __init__(self):
        self.base_url = "https://api.fantasycalc.com"

    def get_calc_rankings(self, isDynasty, numQbs, numTeams, ppr, includeAdp):
        endpoint = f'/values/current?isDynasty={isDynasty}&numQbs={numQbs}&numTeams={numTeams}&ppr={ppr}&includeAdp={includeAdp}'
        full_url = self.base_url + endpoint
        response = requests.get(full_url)
        return response.json()