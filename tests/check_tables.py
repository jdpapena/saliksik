"""Check all tables in the SQLite database."""

import sqlite3

connection = sqlite3.connect("saliksik.db")

tables = connection.execute(
    """
    SELECT name
    FROM sqlite_master
    WHERE type='table'
    ORDER BY name;
    """
).fetchall()

print("Tables:")
for table in tables:
    print(f"- {table[0]}")

connection.close()