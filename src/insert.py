from decouple import config
from tables import projects, tasks


def insert_project(con, project: dict):
    """
    Create a new project into the projects table.
    :param con: Connection to the database.
    :param project: Dictionary object with (name, description, begin_data, end_date) keys.
    :return: project_id
    """
    PROJECTS_TABLE_NAME = config('PROJECTS_TABLE_NAME')
    query = f"""
        INSERT INTO {PROJECTS_TABLE_NAME} {projects.COLUMNS}
        VALUES {tuple(project.values())}
    """
    cur = con.cursor()
    cur.execute(query)
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
    TASKS_TABLE_NAME = config('TASKS_TABLE_NAME')

    query = f"""
        INSERT INTO {TASKS_TABLE_NAME} {tasks.COLUMNS}
        VALUES {tuple(task.values())}
    """
    cur = con.cursor()
    cur.execute(query)
    task_id = cur.lastrowid
    con.commit()
    return task_id
