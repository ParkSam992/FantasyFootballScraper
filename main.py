from RefreshSleeperProjections import refresh_sleeper_projections
from KeepTradeCutScraper import KeepTradeCutSpider
from RefreshDynastyDaddyProjections import refresh_dynasty_daddy_projections
from RefreshFantasyCalcProjections import refresh_fantasy_calc_projections


if __name__ == '__main__':
    # ktcSpider = KeepTradeCutSpider()

    # DynastyDaddy has ktc data
    # ktcSpider.refresh_ktc_rankings()

    refresh_sleeper_projections()
    refresh_dynasty_daddy_projections()
    refresh_fantasy_calc_projections()

    # Add Dynasty Data Lab

    # TODO: Any more data to get? ESPN, Yahoo, Underdog, High stakes money leagues (idk much about these)
    # ESPN and Yahoo seem to not have superflex rankings

    # Some rankings here I can look at another day, though no rankings here yet https://fantasyfootballcalculator.com/adp/2qb/12-team/all






