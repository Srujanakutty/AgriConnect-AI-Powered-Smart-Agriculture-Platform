import sqlite3

conn = sqlite3.connect("database/products.db")

cursor = conn.cursor()

cursor.execute("DELETE FROM products")

conn.commit()

conn.close()

print("All marketplace data cleared successfully.")