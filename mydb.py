import mysql.connector

database = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'Parthu@1974'
)

#prepare a cursor object
cursorObject = database.cursor()

#create a database
cursorObject.execute("CREATE DATABASE elderco")
print("All Done!")
