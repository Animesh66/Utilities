import mysql.connector


def create_db_connection():
    global mydb
    mydb = mysql.connector.connect(
        host="127.0.0.1",  # IP address of the database server
        user="root",
        password="nitaI9093@",
        database="sql_student"
    )


def get_my_sql_query(query):
    mycursor = mydb.cursor()  # This command is to create the Database connection
    mycursor.execute(query)
    # mycursor.execute("SELECT * FROM student")  # This command is going to create a data in
    # the database table
    results = mycursor.fetchone()  # this command will return a row from the table
    return results
    # print(results[0])  # this command will return only the first element of the first row
    # results = mycursor.fetchall()  # the result data will be stored in the results variable
    # for result in results:
    #     print(result)


create_db_connection()
