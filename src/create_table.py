import os
from decouple import config
from src.create_database import create_con


def create_table(con, table_name, table_columns):
    """
    Creates a table in the database.
    :param con: Connection to the database.
    :param table_name: Name of the table.
    :param table_columns: Columns of the table.
    :return: None
    """
    with con:
        cur = con.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS " + table_name + " (" + table_columns + ")")


# For testing purposes
if __name__ == "__main__":
    DATABASE_NAME = config('DATABASE_NAME')

    # get the root directory of the project
    root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    # get the path to the database file
    database_path = os.path.join(root_dir, DATABASE_NAME)

    # create a connection to the database
    con = create_con(database_path)

    with con:
        create_table(con, "projects",
                     "id INTEGER PRIMARY KEY, "
                     "name TEXT NOT NULL, "
                     "begin_date TEXT,"
                     "end_date TEXT")
        create_table(con, "tasks",
                     "id INTEGER PRIMARY KEY, "
                     "name TEXT NOT NULL, "
                     "priority INTEGER NOT NULL, "
                     "status INTEGER NOT NULL, "
                     "project_id INTEGER NOT NULL, "
                     "begin_date TEXT,"
                     "end_date TEXT,"
                     "FOREIGN KEY (project_id) REFERENCES projects(id)")
