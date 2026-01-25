import mysql.connector

try:
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password=input("Enter MySQL password: ")
    )
    print("Connected successfully")

except Exception as e:
    print("Connection failed:", e)

cursor = conn.cursor()

def create_database():
    db_name = input("Enter database name: ")
    try:
       cursor.execute(f"CREATE DATABASE `{db_name}`")
       conn.commit()
       print(f"`{db_name}` database created successfully")

    except Exception as e:
      conn.rollback()
      print("Error:", e)


def create_table():
    name = input("Enter database name inside which you want to create the table: ")
    try:
      cursor.execute(f"USE `{name}`")
      print("Enter your query for table creation: ")
      b=input()
      cursor.execute(b)
      conn.commit()

    except Exception as e:
      conn.rollback()
      print("Error:", e)


def db_show():
    cursor.execute("SHOW DATABASES")
    print("Database list - ")
    for db in cursor:
        print("- ", db[0])


def show_tables():
    try:
      db_name = input("Enter database name: ")
      cursor.execute(f"USE `{db_name}`")
      cursor.execute("SHOW TABLES")
      print("Tables list - ")    
      for db in cursor:
          print("- ", db[0])

    except Exception as e:
      print("Error:", e)


def fetch_table():
    dbname = input("Enter database name: ")
    try:
      cursor.execute(f"USE `{dbname}`")
      cursor.execute("SHOW TABLES")
      print("Tables list - ")    
      for db in cursor:
          print("- ", db[0])
      print("Enter the table name from above: ")
      a=input()
      cursor.execute(f"SELECT* FROM `{a}`")
      a=cursor.fetchall()
      for row in a:
          print(row)

    except Exception as e:
      print("Error:", e)

while True:

    a=int(input("""- Enter 1 for creating database.
- Enter 2 for creating table inside a selected database.
- Enter 3 for Showing Databases
- Enter 4 for Showing Tables
- Enter 5 for a Fetching Table 
- Enter 0 to exit
Enter choice: """))

    if(a==1):
        create_database()

    elif(a==2):
        create_table()

    elif(a==3):
        db_show()

    elif(a==4):
        show_tables()

    elif(a==5):
        fetch_table()

    elif a == 0:
        print("Exiting...")
        break

else:
   print("Invalid arguments")

conn.close()

