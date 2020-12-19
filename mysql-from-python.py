import pymysql

# Connect to the database
connection = pymysql.connect(host='localhost',
                             db='Chinook')


try:
    # Run a query
    with connection.cursor() as cursor:
        rows = [(23, 'Bob'),
                (24, 'Jim'),
                (25, 'Fred')]
        cursor.executemany("UPDATE Friends SET age = %s WHERE name = %s;",
                        rows)
        connection.commit()
finally:
    # Close the connection, regardless of whether the above was successful
    connection.close()

