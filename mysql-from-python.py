import datetime
import pymysql

# Connect to the database
connection = pymysql.connect(host='localhost',
                             db='Chinook')


try:
    # Run a query
    with connection.cursor() as cursor:        
        cursor.execute("UPDATE Friends SET age = 22 WHERE name = 'Bob';")
        connection.commit()
finally:
    # Close the connection, regardless of whether the above was successful
    connection.close()

