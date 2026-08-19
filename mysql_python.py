import mysql.connector 
from mysql.connector import Error

connection = None

try:

    connection = mysql.connector.connect( #connection establishment
        host = 'localhost',
        database = 'UBER',
        user = 'root',
        password = 'root'
    )

    if connection.is_connected():

        print("Connection is established")
    cursor = connection.cursor()

    query = 'SELECT * FROM UBER.Accounts;' 

    cursor.execute(query)

    rows = cursor.fetchall()

    for i in rows:
        print(i)
    
except Error as e:
    print ("Connection is not established")

finally:
    if connection is not None and connection.is_connected():
        cursor.close()
        connection.close()

        print("MySQL connection is closed")

# Result: 

#Connection is established
#(1, 'Alice', Decimal('4000.00'))
#MySQL connection is closed