import importlib

from decouple import config
from tables import projects, tasks


def insert(con, table_name: str, data: dict):
    """
    Create a new project into the projects table.
    :param con: Connection to the database.
    :param table_name: Name of the table.
    :param data: Data to insert.
    :return: row_id of the inserted row.
    """
    tables = "tables." + table_name
    table = importlib.import_module(tables)
    table_columns = table.COLUMNS

    query = f"""
        INSERT INTO {table_name} {table_columns}
        VALUES {tuple(data.values())}
    """
    cur = con.cursor()
    cur.execute(query)
    row_id = cur.lastrowid
    con.commit()
    return row_id
