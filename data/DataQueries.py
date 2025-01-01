from.DataAccess import DataAccess
from datetime import datetime, timezone

class DataQueries(DataAccess):

    def clear_ktc_data(self):
        query = 'DELETE FROM "KeepTradeCutRanking";'
        self.run_sql(query)

    def insert_ktc_data(self, id, first_name, last_name, position, ranking_one_qb, ranking_two_qb, json):
        query = f'''
            INSERT INTO "KeepTradeCutRanking" ("Id", "FirstName", "LastName", "Position", "RankingOneQB", "RankingTwoQB", "Resource", "UpdatedAt")
            VALUES ('{id}', '{first_name}', '{last_name}', '{position}', '{ranking_one_qb}', '{ranking_two_qb}', '{json}', '{datetime.now(timezone.utc)}');
        '''
        self.run_sql(query)

    def clear_sleeper_data(self):
        query = 'DELETE FROM "SleeperRankings";'
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

    def clear_dynasty_daddy_data(self):
        query = 'DELETE FROM "DynastyDaddyMarketRankings";'
        self.run_sql(query)

    def insert_dynasty_daddy_data(self, name_id, market, overall_rank, sf_overall_rank, resource):
        query = f'''
            INSERT INTO "DynastyDaddyMarketRankings" ("NameId", "Market", "OverallRank", 
                                          "SFOverallRank", "Resource", "UpdatedAt") 
            VALUES ('{name_id}', '{market}', '{overall_rank}', '{sf_overall_rank}', 
                    '{resource}', '{datetime.now(timezone.utc)}');
        '''
        self.run_sql(query)

    def clear_dd_player_data(self):
        query = 'DELETE FROM "DynastyDaddyPlayerData";'
        self.run_sql(query)

    def insert_dynasty_daddy_player_data(self, name_id, sleeper_id, first_name, last_name, position, player):
        query = f'''
            INSERT INTO "DynastyDaddyPlayerData" ("NameId", "SleeperId", "FirstName", "LastName", 
                                      "Position", "Resource", "UpdatedAt") 
            VALUES ('{name_id}', '{sleeper_id}', '{first_name}', '{last_name}',
                    '{position}', '{player}', '{datetime.now(timezone.utc)}');
        '''
        self.run_sql(query)