import sqlite3

connection = sqlite3.connect("saliksik.db")
cursor = connection.cursor()

print("\n=== TABLES ===\n")

for (table_name,) in cursor.execute("""
    SELECT name
    FROM sqlite_master
    WHERE type='table'
    ORDER BY name
"""):
    print(table_name)

print("\n=== COMPANY DIRECTORY COUNT ===\n")

try:
    count = cursor.execute(
        "SELECT COUNT(*) FROM company_directory"
    ).fetchone()[0]

    print(count)

except sqlite3.OperationalError:
    print("company_directory table not found!")

connection.close()