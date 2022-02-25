import os

from decouple import config

from src.create_database import create_con
from src.create_table import create_table
from src.insert import insert
from src.update import update
from src.select_from import select_all, select_task_by_priority
from src.delete import delete_using_id, delete_all
from tables import projects, tasks

DATABASE_NAME = config('DATABASE_NAME')
PROJECTS_TABLE_NAME = config('PROJECTS_TABLE_NAME')
TASKS_TABLE_NAME = config('TASKS_TABLE_NAME')
PROJECTS_FAKE_DATA = (
    ("Project 1", "2015-01-01", "2015-01-31"),
    ("Project 2", "2015-02-01", "2015-02-28"),
    ("Project 3", "2015-03-01", "2015-03-31"),
)
TASKS_FAKE_DATA = (
    ("Task 1", 3, 1, 1, "2015-01-01", "2015-01-31"),
    ("Task 2", 2, 2, 1, "2015-01-01", "2015-01-31"),
    ("Task 3", 3, 3, 1, "2015-01-01", "2015-01-31"),
)


def main():
    # get the root directory of the project
    root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    # get the path to the database file
    database_path = os.path.join(root_dir, DATABASE_NAME)
    # 1. create a connection to the database
    con = create_con(database_path)

    with con:
        # 2. create the table
        create_table(con, PROJECTS_TABLE_NAME, projects.STRUCTURE)
        create_table(con, TASKS_TABLE_NAME, tasks.STRUCTURE)

        # 3. insert some data
        for idx, project_data in enumerate(PROJECTS_FAKE_DATA):
            project = {key: value for key, value in zip(projects.COLUMNS, project_data)}
            insert(con, PROJECTS_TABLE_NAME, project)

        for idx, task_data in enumerate(TASKS_FAKE_DATA):
            task = {key: value for key, value in zip(tasks.COLUMNS, task_data)}
            insert(con, TASKS_TABLE_NAME, task)

        # 4. Update the data for the first project and the first task
        update(con, PROJECTS_TABLE_NAME, 1, {"name": "RZ"})
        update(con, TASKS_TABLE_NAME, 1, {"name": "Z"})

        # 5. Select the data
        for i in select_all(con, PROJECTS_TABLE_NAME):
            print(i)

        for i in select_all(con, TASKS_TABLE_NAME):
            print(i)

        for i in select_task_by_priority(con, 3):
            print(i)

        # 6. Delete the data
        print(delete_using_id(con, PROJECTS_TABLE_NAME, 2))
        delete_using_id(con, TASKS_TABLE_NAME, 3)
        print(delete_all(con, TASKS_TABLE_NAME))
        delete_all(con, PROJECTS_TABLE_NAME)


if __name__ == "__main__":
    main()
