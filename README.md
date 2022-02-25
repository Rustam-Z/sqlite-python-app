# Python & SQL

Objectives:
1. Create a database / connect to existing database
2. Create a table / get existing table
3. Insert values
4. Update values
5. Select values
6. Delete data

Useful commands:
```
con = sqlite3.connect("example.db")  # ":memory:"
cur = conn.cursor()  # Cursor = makes the connection for executing SQL queries
cur.execute("...")  # SELECT FROM, CREATE TABLE, INSERT INTO
cur.executemany("...(?, ?)", data)  # data can be tuple or dict
cur.fetchall()
cur.lastrowid
con.commit()
con.close()
```

## To read
- https://docs.python.org/3/library/sqlite3.html
