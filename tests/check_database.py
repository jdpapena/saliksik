import sqlite3

connection = sqlite3.connect("saliksik.db")
cursor = connection.cursor()

print("\nCompanies\n")

for ticker, name in cursor.execute(
    "SELECT ticker, name FROM companies ORDER BY ticker"
):
    print(f"{ticker:<8} {name}")

connection.close()
