import sqlite3


def delete_using_id(con, table_name: str, id: int):
    """
    Delete a row by id in any table.
    :param con:  Connection to the SQLite database.
    :param table_name: Name of the table.
    :param id: id of the task
    :return: Number of rows deleted.
    """
    query = f"DELETE FROM {table_name} WHERE id=?"
    cur = con.cursor()
    try:
        cur.execute(query, (id,))
        con.commit()
    except sqlite3.Error as e:
        print(e)

    return cur.rowcount


def delete_all(con, table_name: str):
    """
    Delete all rows in the tasks table.
    :param con: Connection to the SQLite database.
    :param table_name: Name of the table.
    :return: Number of rows deleted.
    """
    query = f"DELETE FROM {table_name}"
    cur = con.cursor()
    try:
        cur.execute(query)
        con.commit()
    except sqlite3.Error as e:
        print(e)

    return cur.rowcount

