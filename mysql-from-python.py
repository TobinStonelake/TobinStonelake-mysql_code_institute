import pymysql

# Connect to the database
connection = pymysql.connect(host='localhost',
                             db='Chinook')


try:
    # Run a query
    with connection.cursor() as cursor:
        rows = cursor.executemany("DELETE FROM Friends WHERE name = %s;", ['Bob', 'Jim'])
        connection.commit()
finally:
    # Close the connection, regardless of whether the above was successful
    connection.close()

