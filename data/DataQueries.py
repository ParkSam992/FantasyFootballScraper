from.DataAccess import DataAccess
from datetime import datetime, timezone

class DataQueries(DataAccess):

    def clear_ktc_data(self):
        query = 'delete from "KeepTradeCutRanking";'
        self.run_sql(query)

    def insert_ktc_data(self, id, first_name, last_name, position, ranking_one_qb, ranking_two_qb, json):
        query = f'''
            INSERT INTO "KeepTradeCutRanking" ("Id", "FirstName", "LastName", "Position", "RankingOneQB", "RankingTwoQB", "Resource", "UpdatedAt")
            VALUES ('{id}', '{first_name}', '{last_name}', '{position}', '{ranking_one_qb}', '{ranking_two_qb}', '{json}', '{datetime.now(timezone.utc)}');
        '''
        self.run_sql(query)

    def clear_sleeper_data(self):
        query = 'delete from "SleeperRankings";'
        self.run_sql(query)

    def insert_sleeper_data(self, id, first_name, last_name, position, stats, json):
        query = f'''
            INSERT INTO "SleeperRankings" ("Id", "FirstName", "LastName", "Position", 
                               "ADP2QB", "ADPDynasty", "ADPDynasty2QB", "ADPDynastyHalfPPR", 
                               "ADPDynastyPPR", "ADPDynastyStandard","ADPHalfPPR", 
                               "ADPFullPPR", "ADPRookie", "ADPStandard", "Resource", "UpdatedAt") 
            VALUES ('{id}', '{first_name}', '{last_name}', '{position}', '{stats['adp_2qb']}', 
                    '{stats['adp_dynasty']}', '{stats['adp_dynasty_2qb']}', '{stats['adp_dynasty_half_ppr']}', 
                    '{stats['adp_dynasty_ppr']}', '{stats['adp_dynasty_std']}', '{stats['adp_half_ppr']}', 
                    '{stats['adp_ppr']}', '{stats['adp_rookie']}', '{stats['adp_std']}', '{json}', 
                    '{datetime.now(timezone.utc)}');
        '''
        self.run_sql(query)
