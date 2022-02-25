import sqlite3


def is_id_exists(con, table, id):
    try:
        obj = con.execute(f"SELECT * FROM {table} WHERE id = {id}")
    except sqlite3.Error as e:
        print("Error: {}".format(e))
        return False
    return obj.fetchone()


def update_project(con, project_id, new_values):
    """
    Update a project in the database.

    :param con: Database connection.
    :param project_id: Project ID which needs to be updated.
    :param new_values: Dict with the new values, you don't need to specify the columns you don't want to change.
    :return: True if the update was successful, False otherwise.
    """
    table_name = "projects"
    table_columns = ("name", "begin_date", "end_date")

    # Check if the project exists
    obj = is_id_exists(con, table_name, project_id)

    if not obj:
        return False

    # Overwrite project_as_dict with new_values
    project_as_dict = {key: value for key, value in zip(table_columns, obj[1:])}  # We don't need the first column
    print(">> project_as_dict", project_as_dict)
    project_as_dict.update(new_values)

    try:
        con.execute(f"UPDATE {table_name} SET name = ?,  begin_date = ?, end_date = ? WHERE id = ?", (
            project_as_dict['name'],
            project_as_dict['begin_date'],
            project_as_dict['end_date'],
            project_id))
    except sqlite3.Error as e:
        print("Error: {}".format(e))
        return False
    return True


def update_task(con, task_id, new_values):
    table_columns = ("name", "priority", "status", "project_id", "begin_date", "end_date")
