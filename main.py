from RefreshSleeperProjections import refresh_sleeper_projections
from KeepTradeCutScraper import KeepTradeCutSpider
from RefreshDynastyDaddyProjections import refresh_dynasty_daddy_projections


if __name__ == '__main__':
    ktcSpider = KeepTradeCutSpider()

    # DynastyDaddy has ktc data
    # ktcSpider.refresh_ktc_rankings()

    refresh_sleeper_projections()
    refresh_dynasty_daddy_projections()
    # TODO: Any more data to get? ESPN, Yahoo, Underdog, High stakes money leagues (idk much about these)
    # ESPN and Yahoo seem to not have superflex rankings

    # Some rankings here I can look at another day, though no rankings here yet

    # TODO: After refreshing, might need to do some sort of ID mapping table
    #       since not all names are the same between places





