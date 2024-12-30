from RefreshSleeperProjections import refresh_sleeper_projections
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from KeepTradeCutScraper import KeepTradeCutSpider

def refresh_ktc_rankings():
    process = CrawlerProcess(get_project_settings())
    process.crawl(KeepTradeCutSpider)
    process.start()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    refresh_ktc_rankings()
    refresh_sleeper_projections()




