def insert_project(con, project):
    """
    Create a new project into the projects table.
    :param con: Connection to the database.
    :param project: Dictionary object with (name, description, begin_data, end_date) keys.
    :return: project_id
    """

    query = """
        INSERT INTO projects (name, begin_date, end_date)
        VALUES (?, ?, ?)
    """
    cur = con.cursor()
    cur.execute(query, (project['name'],
                        project['begin_date'],
                        project['end_date']))
    project_id = cur.lastrowid
    con.commit()
    return project_id


def insert_task(con, task):
    """
    Create a new task into the tasks table.
    :param con: Connection to the database.
    :param task: Dictionary object with (name, priority, PROJECT_ID (Project object), status_id, begin_date, end_date) keys.
    :return: task_id
    """

    query = """
        INSERT INTO tasks ("name", "priority", "status", "project_id", "begin_date", "end_date")
        VALUES (?, ?, ?, ?, ?, ?)
    """
    cur = con.cursor()
    cur.execute(query, (task['name'],
                        task['priority'],
                        task['status'],
                        task['project_id'],
                        task['begin_date'],
                        task['end_date']))
    task_id = cur.lastrowid
    con.commit()
    return task_id
