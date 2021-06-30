import mysql.connector


def create_db_connection():
    mydb = mysql.connector.connect(
        host="127.0.0.1",  # IP address of the database server
        user="root",
        password="nitaI9093@",
        database="sql_student"
    )
    mycursor = mydb.cursor()  # This command is to create the Database connection
    mycursor.execute("INSERT INTO student VALUES(28, 'Tweety', 1)")
    mycursor.execute("SELECT * FROM student")  # This command is going to create a data in
    # the database table
    results = mycursor.fetchall()  # the result data will be stored in the results variable
    for result in results:
        print(result)


create_db_connection()
