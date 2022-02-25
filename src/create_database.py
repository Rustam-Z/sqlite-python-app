"""
Create a database for the application.
If the database already exists, it will return that database, else new database will be created.
"""

import os
import sqlite3
from decouple import config


def create_con(db_name):
    """
    Create a connection to the database.
    :param db_name: Name of the database.
    """
    try:
        con = sqlite3.connect(db_name)
        return con
    except sqlite3.Error as e:
        print(e)


if __name__ == "__main__":
    DATABASE_NAME = config('DATABASE_NAME')

    # Get the root of the project
    root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    # Get the path to the database file in the project
    database_path = os.path.join(root_dir, DATABASE_NAME)

    print(root_dir, database_path)

    # Create a database connection
    con = create_con(DATABASE_NAME)

    with con:
        print("Database created successfully.")
        print("Database version: {}".format(sqlite3.version))
