import sqlite3
import importlib


def is_id_exists(con, table, id):
    try:
        obj = con.execute(f"SELECT * FROM {table} WHERE id = {id}")
    except sqlite3.Error as e:
        print("Error: {}".format(e))
        return False
    return obj.fetchone()


def update(con, table_name, id, data):
    """
    Update any table in the database.

    :param con: Database connection.
    :param table_name: Table name.
    :param id: ID which needs to be updated.
    :param data: Dict with the new values, you don't need to specify the columns you don't want to change.
    :return: True if the update was successful, False otherwise.
    """
    tables = "tables." + table_name
    table = importlib.import_module(tables)
    table_columns = table.COLUMNS

    # Check if the project exists
    obj = is_id_exists(con, table_name, id)

    if not obj:
        return False

    # Overwrite project_as_dict with new_values
    obj_as_dict = {key: value for key, value in zip(table_columns, obj[1:])}  # We don't need the first column
    obj_as_dict.update(data)
    obj_as_str = ",".join(f"{key} = '{value}'" for key, value in obj_as_dict.items())

    try:
        query = f"UPDATE {table_name} SET {obj_as_str} WHERE id = {id}"
        con.execute(query)
    except sqlite3.Error as e:
        print("Error: {}".format(e))
        return False
    return True
