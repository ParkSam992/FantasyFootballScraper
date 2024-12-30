import psycopg2
import pandas as pd
from tabulate import tabulate

class DataAccess:
    def __init__(self):
        # self.config = config(filename=fileName, env=env)
        # if database:
        #     self.config['database'] = database
        # self.conn = psycopg2.connect(**self.config)
        self.conn = psycopg2.connect(dbname="postgres", user="sampark99", password="password", host="localhost", port="5432")
        self.cursor = self.conn.cursor()

    def __del__(self):
        self.cursor.close()
        self.conn.close()

    def print_table(self, table):
        print(tabulate(table, headers='keys', tablefmt='psql'))

    def create_pandas_table(self, query, printResults=False):
        table = pd.read_sql_query(query, self.conn)
        if printResults:
            self.print_table(table)
        return table

    def run_sql(self, query):
        try:
            self.cursor.execute(query)
            self.conn.commit()
        except psycopg2.errors.InvalidTextRepresentation as e:
            self.conn.rollback()
            raise e
