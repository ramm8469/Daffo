import sqlite3

# create a connection object
conn = sqlite3.connect("test.db")

# to create tables in the database
# conn.execute(''' 
# create table users (
#   name text,
#   age integer,
#   branch text
# );
# ''')

# insert record to the user table
# conn.execute("insert into users(name,age,branch) values('ram',23,'IT')")


# Now, commit to save the data to the database
# conn.commit()

# to read data create a cursor
cursor = conn.execute("select * from users")

# print the data from the cursor
for row in cursor:
  print(row)
  
