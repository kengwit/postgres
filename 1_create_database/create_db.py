import psycopg2

#establishing the connection
conn = psycopg2.connect(
   database="postgres", user='postgres', password='1234', host='localhost', port= '5432'
)
conn.autocommit = True

#Creating a cursor object using the cursor() method
cursor = conn.cursor()

db_name = 'mydb'
cursor.execute('DROP DATABASE IF EXISTS ' + db_name )

#Preparing query to create a database
sql = 'CREATE DATABASE ' + db_name
cursor.execute(sql)


print("Database created successfully........")

#Preparing query to create a database
sql = 'DROP DATABASE ' + db_name

#delete
cursor.execute(sql)

#Closing the connection
conn.close()
