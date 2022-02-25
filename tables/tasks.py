COLUMNS = ("name", "priority", "status", "project_id", "begin_date", "end_date")

STRUCTURE = "id integer PRIMARY KEY," \
            "name TEXT NOT NULL, " \
            "priority INTEGER NOT NULL, " \
            "status INTEGER NOT NULL, " \
            "project_id INTEGER NOT NULL, " \
            "begin_date TEXT," \
            "end_date TEXT," \
            "FOREIGN KEY (project_id) REFERENCES projects(id)"

