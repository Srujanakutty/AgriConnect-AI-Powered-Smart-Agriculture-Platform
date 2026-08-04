import sqlite3
import os

# ensure database folder exists
if not os.path.exists("database"):
    os.makedirs("database")

conn = sqlite3.connect("database/products.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS products(
id INTEGER PRIMARY KEY AUTOINCREMENT,
crop_name TEXT,
price TEXT,
quantity TEXT,
farmer_name TEXT,
contact TEXT,
location TEXT
)
""")

conn.commit()
conn.close()

print("Database created successfully")