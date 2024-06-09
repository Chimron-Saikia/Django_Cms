import mysql.connector

dataBase=mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='Chim@1234'
)

cursorObject=dataBase.cursor()

cursorObject.execute("CREATE DATABASE mydatabase")
print("All Done")