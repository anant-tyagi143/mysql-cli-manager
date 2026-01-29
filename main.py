import mysql.connector

try:
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password=input("Enter MySQL password: ")
    )
    print("Connected successfully")
    cursor = conn.cursor()

except Exception as e:
    print("Connection failed:", e)
    exit()

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


def deletion():
    i=int(input('''What do you want to delete?
- 1 for Deleting a Database
- 2 for Deleting a Table
Enter your choice: '''))
    if(i==1):
       try:
          cursor.execute("SHOW DATABASES")
          print("Database list - ")
          a = cursor.fetchall()
          for db in a:
             print("- ", db[0]) 
          db_name=input("Enter database name from above to delete: ")
          cursor.execute(f"DROP DATABASE `{db_name}`")
          print(f"Database {db_name} has been deleted successfully")
       except Exception as e:
          print("Error:", e)

    elif(i==2):
       try:
         db_name = input("Enter database name: ")
         cursor.execute(f"USE `{db_name}`")
         cursor.execute("SHOW TABLES")
         print("Tables list - ")    
         a = cursor.fetchall()
         for db in a:
             print("- ", db[0]) 
         table=input("Enter table name from above to delete: ")
         cursor.execute(f"DROP `{table}`")
         print(f"Table {table} has been deleted successfully")

       except Exception as e:
          print("Error:", e)


def get_table():
    try:
        db_name=input("Enter the database: ")
        cursor.execute(f"USE `{db_name}` ")
        cursor.execute("SHOW TABLES") 
        a = cursor.fetchall()
        if not a:
           print("No tables found.")

        print("Tables list - ")   
        for db in a:
             print("- ", db[0]) 
        table=input("Enter table name from above to update: ")
        return table
    except Exception as e:
        print("Error:", e)
        return None

def alter_table():
    i=int(input('''- 1 for Add new Column
- Enter 2 for Changing the datatype of an existing column.
- Enter 3 for Renaming a Column
- Enter 4 for Deleting a Column
- Enter 5 for Renaming the Table
- Enter 6 for Assigning Primary Key to an column
- Enter 7 for Assigning NOT NULL to an column
                
Enter your choice: '''))
    
    if(i==1):
        try:
         table=get_table()
         column_name=input("Enter the name of New column: ")
         datatype = input("Enter datatype (e.g. INT, VARCHAR(225), FLOAT): ")
         cursor.execute(f"ALTER TABLE `{table}` ADD `{column_name}` {datatype}")
         conn.commit()
         print("✅ Column modified")
        except Exception as e:
            print("Error:", e)
            conn.rollback()

    elif(i==2):
        try:
         table=get_table()
         column_name=input("Enter the column name whose datatype you want to change: ")
         datatype=input("Enter the new datatype to change: ")
         cursor.execute(f"ALTER TABLE `{table}` MODIFY `{column_name}` {datatype}")
         conn.commit()
         print("✅ Column modified")
        except Exception as e:
            print("Error:", e)
            conn.rollback()

    elif(i==3):
        try:
         table=get_table()
         column_name=input("Enter the column name: ")
         newname=input("Enter the new column name to change : ")
         datatype=input("Enter datatype (e.g. INT, VARCHAR(225), FLOAT): ")
         cursor.execute(f"ALTER TABLE `{table}` CHANGE `{column_name}` `{newname}` {datatype}")
         conn.commit()
         print("✅ Column modified")
        except Exception as e:
            print("Error:", e)
            conn.rollback()

    elif(i==4):
        try:
         table=get_table()
         column_name=input("Enter the column name for deletion: ")
         cursor.execute(f"ALTER TABLE `{table}` DROP `{column_name}`")
         conn.commit()
         print("✅ Column modified")
        except Exception as e:
            print("Error:", e)
            conn.rollback()

    elif(i==5):
        try:
         table=get_table()
         table_newname=input("Enter the New Table name for renaming: ")
         cursor.execute(f"ALTER TABLE `{table}` RENAME TO `{table_newname}`")
         conn.commit()
         print("✅ Column modified")
        except Exception as e:
            print("Error:", e)
            conn.rollback()

    elif(i==6):
        try:
         table=get_table()
         column_name=input("Enter the column name for assigning primary key: ")
         cursor.execute(f"ALTER TABLE `{table}` ADD PRIMARY KEY `{column_name}`")
         conn.commit()
         print("✅ Column modified")
        except Exception as e:
            print("Error:", e)
            conn.rollback()
    
    elif(i==7):
        try:
         table=get_table()
         column_name=input("Enter the column name: ")
         datatype=input("Enter the datatype of the column: ")
         cursor.execute(f"ALTER TABLE `{table}` MODIFY `{column_name}` {datatype} NOT NULL")
         conn.commit()
         print("✅ Column modified")
        except Exception as e:
            print("Error:", e)
            conn.rollback()

    else: 
        print("Invalid selection")

def alter_table_values():
    database=input("Enter the database: ")
    cursor.execute(f"USE {database} ")
    table=input("Enter the table name in which you want to insert values: ")
    value=input("Enter the value to update: ")
    where=input("Enter where you want to change the value: ")
    cursor.execute(f"UPDATE {table} SET {value} WHERE {where}")

def aggregate_fun():
    i=int(input('''
- Enter 1 for using COUNT function
- Enter 2 for using SUM function
- Enter 3 for using AVG function
- Enter 4 for using MIN function
- Enter 5 for using MAX function
          
Enter your choice: 
'''))
    if(i==1):
        table=get_table()
        column = input("Enter column name or * for all rows: ")
        if column == "*":
            cursor.execute(f"SELECT COUNT(*) FROM {table}")
        else:
            cursor.execute(f"SELECT COUNT({column}) FROM {table}")
        result = cursor.fetchone()
        print("Result:", result[0])

    elif(i==2):
        table=get_table()
        column_name=input("Enter the column name on which to use SUM func: ")
        cursor.execute(f"SELECT SUM({column_name}) FROM {table} ")
        result = cursor.fetchone()
        print("Result:", result[0])

    elif(i==3):
        table=get_table()
        column_name=input("Enter the column name on which to use AVG func: ")
        cursor.execute(f"SELECT AVG({column_name}) FROM {table} ")
        result = cursor.fetchone()
        print("Result:", result[0])

    elif(i==4):
        table=get_table()
        column_name=input("Enter the column name on which to use MIN func: ")
        cursor.execute(f"SELECT MIN({column_name}) FROM {table} ")  
        result = cursor.fetchone()
        print("Result:", result[0])

    elif(i==5):
        table=get_table()
        column_name=input("Enter the column name on which to use MAX func: ")
        cursor.execute(f"SELECT MAX({column_name}) FROM {table} ")  
        result = cursor.fetchone()
        print("Result:", result[0])

    else:
        print("Invalid arguments")

while True:

    a=int(input('''
- Enter 1 for creating database.
- Enter 2 for creating table inside a selected database.
- Enter 3 for Showing Databases
- Enter 4 for Showing Tables
- Enter 5 for Fetching Table 
- Enter 6 for Deletion
- Enter 7 for Altering Table
- Enter 8 for Altering Table Values
- Enter 9 for using Aggregate functions
- Enter 0 to exit
                
Enter choice: '''))

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
    
    elif(a==6):
        deletion()

    elif(a==7):
        alter_table()

    elif(a==8):
        alter_table_values()

    elif(a==9):
        aggregate_fun()

    elif(a==0):
        print("Exiting...")
        break

    else:
        print("Invalid arguments")

conn.close()

