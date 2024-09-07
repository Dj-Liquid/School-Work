!pip install mysql-connector-python

import mysql.connector

try:
  connection = mysql.connector.connect(
      host = "database-comp3162.cqb8o27401uq.us-east-2.rds.amazonaws.com",
      user = "comp3162user",
      password = "Password876",
      port = 3306,
      database = "comp3162"
  )

  print("Connected to MYSQL database successfully")
  print("\n")

  cursor = connection.cursor()
  cursor.execute("SELECT * FROM Patients")
  rows = cursor.fetchall()
  for row in rows:
    formatted_row = [col if col is not None else 'NULL' for col in row]
    print(formatted_row)

  cursor.close()
  connection.close()

except mysql.connector.Error as error:
  print("Error connecting to MYSQL database:", error)