import sqlite3

conn = sqlite3.connect("my_database.db")
cursor = conn.cursor()
cursor.execute("SELECT sqlite_version();")
print(f"SQLite version: {cursor.fetchone()[0]}")
conn.close()