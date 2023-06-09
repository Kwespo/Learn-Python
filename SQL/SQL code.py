import sqlite3

connection = sqlite3.Connection("SQL\database\mydatabase.db")

cursor = connection.cursor()

"""
def maketable():
  
  command1 = "CREATE TABLE IF NOT EXISTS main(id INTEGER PRIMARY KEY, name TEXT, colour TEXT)"

  cursor.execute(command1)

  #________________Adds a new column to the SQL table with; id = 6, name = test 6 and colour = purpol_____________________________

  cursor.execute("INSERT INTO main Values(6, 'test_6', 'purpol')")

  connection.commit()

maketable()
"""


"""Queries in python"""

#ALL

cursor.execute("SELECT * FROM main")
results = cursor.fetchall()
print("all", results)

#SPESIFIC

cursor.execute("SELECT * FROM main WHERE name = 'test_2'")
results = cursor.fetchall()
print("Just name is test 2", results)
