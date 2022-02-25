def delete_with_id(con, table: str, id: int):
    """
    Delete a row by id in any table
    :param con:  Connection to the SQLite database
    :param id: id of the task
    :return:
    """
    query = f"DELETE FROM {table} WHERE id=?"
    cur = con.cursor()
    cur.execute(query, (id,))
    con.commit()


def delete_all(con, table):
    """
    Delete all rows in the tasks table
    :param con: Connection to the SQLite database
    :return:
    """
    query = f"DELETE FROM {table}"
    cur = con.cursor()
    cur.execute(query)
    con.commit()
