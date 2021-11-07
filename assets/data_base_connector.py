import sqlite3
import pathlib

class DataBaseConnector:
    """ Connector provide connect between database and inteface """

    def __init__(self, file: str) -> None:
        self.root_path = pathlib.Path().absolute()
        self.db_path = self.root_path.joinpath('db').joinpath(file)
