import requests

class SleeperApi:
    def __init__(self):
        self.base_url = 'https://api.sleeper.com'

    def get_projections_data(self, year, season_type = "regular"):
        # season_type options: couldn't find anything other than "regular"
        # want to get all positions always, will filter out in the db
        endpoint = f'/projections/nfl/{year}?season_type={season_type}&position[]=DEF&position[]=K&position[]=QB&position[]=RB&position[]=TE&position[]=WR'
        full_url = self.base_url + endpoint
        response = requests.get(full_url)
        return response.json()
