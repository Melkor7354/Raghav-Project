import mysql.connector

# Creating connection object
mydb = mysql.connector.connect(
    host='localhost:1433',
    user='root',
    password='Crisronaldo@7'
)

# Printing the connection object
print(mydb)