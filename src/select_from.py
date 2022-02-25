def select_all(con, table: str):
    """
    Query all rows in the tasks table.
    :param con: the Connection object
    :return:
    """
    cur = con.cursor()
    cur.execute(f"SELECT * FROM {table}")
    rows = cur.fetchall()
    yield from rows


def select_task_by_priority(con, priority):
    """
    Query tasks by priority.
    :param con: the Connection object
    :param priority:
    :return:
    """
    cur = con.cursor()
    cur.execute("SELECT * FROM tasks WHERE priority=?", (priority,))
    rows = cur.fetchall()
    yield from rows
