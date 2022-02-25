def select_all(con, table_name: str):
    """
    Query all rows in the tasks table.
    :param con: Connection object.
    :param table_name: Name of the table.
    :return: A generator object.
    """
    cur = con.cursor()
    cur.execute(f"SELECT * FROM {table_name}")
    rows = cur.fetchall()
    yield from rows


def select_task_by_priority(con, priority):
    """
    Query tasks by priority.
    :param con: the Connection object.
    :param priority: The level of priority in tasks.
    :return: A generator object.
    """
    cur = con.cursor()
    cur.execute("SELECT * FROM tasks WHERE priority=?", (priority,))
    rows = cur.fetchall()
    yield from rows
