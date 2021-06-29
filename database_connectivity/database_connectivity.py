import mysql.connector

def create_db_connection:

mydb = mysql.connector.connect(
    host="localhost",  # IP address of the database server
    user="root",
    password="root",
    database="sql_student"
)

mycursor = mydb.cursor()
mycursor.execute("INSERT INTO student VALUES(2, 'Tweety', NULL)")
results =mycursor.fetchall()
for result in results:
    print(result)