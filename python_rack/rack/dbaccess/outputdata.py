import sqlite3

# Create a connection object to the database
conn = sqlite3.connect("/Users/gaoshihui/rack_py_g/rack_py_g/rack-py-main/rack/dbaccess/rack-python.db")

# Create a cursor object from the connection
cursor = conn.cursor()

# Execute an SQL command to select all data from a table
cursor.execute('SELECT * FROM CodeToken')

# Fetch the results of the query
results = cursor.fetchall()

# Print the results
for row in results:
    print(row)



cursor.execute('SELECT * FROM TextToken')

# Fetch the results of the query
results2 = cursor.fetchall()

# Print the results
for row in results2:
    print(row)

# Close the cursor and the connection
cursor.close()
conn.close()