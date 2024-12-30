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

