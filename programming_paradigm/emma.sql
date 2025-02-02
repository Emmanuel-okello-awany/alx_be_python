import mysql.connector


mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="A@dapemmizo1",
    database=""
)

print(mydb.get_server_info())