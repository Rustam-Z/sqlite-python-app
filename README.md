# Python & SQL
Using clean code principles and DRY. If you need to change the table's structure in the future, go ahead and add the things you need in `tables` directory. All changed will be sync in insert, update transactions.


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
