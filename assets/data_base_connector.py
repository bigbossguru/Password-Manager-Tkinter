import sqlite3
import pathlib
from typing import List

class DataBaseConnector:
    """ Connector provide connect between database and inteface """

    def __init__(self, file: str) -> None:
        self.root_path = pathlib.Path().absolute()
        self.db_path = self.root_path.joinpath('db').joinpath(file)

    def __enter__(self):
        self.conn = sqlite3.connect(self.db_path)
        self.cur = self.conn.cursor()
        return self

    def create_table(self, contain: str):
        self.cur.execute(contain)
        self.conn.commit()
    
    def insert_data(self, contain: str, *args):
        self.cur.execute(contain, *args)
        self.conn.commit()

    def fetch_info(self) -> List:
        pass

    def __exit__(self, *args):
        self.conn.close()