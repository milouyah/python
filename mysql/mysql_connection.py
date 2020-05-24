import mysql.connector

def connect(host='localhost', id='root', passwd=None, dbname=None):
    try:
        global mydb
        mydb = mysql.connector.connect(
            host=host,
            user=id,
            #passwd="yourpassword",
            database=dbname
        )
    except Exception as e:
        print(e)

def create_database(name, charset='utf8'):
    try:
        sql = f"CREATE DATABASE {name} CHARACTER SET = {charset}"
        #print(sql)
        cursor = mydb.cursor()
        cursor.execute(sql)
        return 0
    except Exception as e:
        print(e)
        return -1
    
def drop_database(name):
    try:
        sql = f"DROP DATABASE {name}"
        print(sql)
        cursor = mydb.cursor()
        cursor.execute(sql)
        return 0
    except Exception as e:
        print(e)
        return -1

def create_table(name,fields=None):
    try:
        if fields==None:
            fields = "name VARCHAR(255), address VARCHAR(255)"
        sql = f"CREATE TABLE {name} ({fields})"
        print(sql)
        cursor = mydb.cursor()
        cursor.execute(sql)
        return 0
    except Exception as e:
        print(e)
        return -1
    
def select_data():
    None



    
def drop_table(name):
    try:
        sql = f"DROP TABLE {name}"
        print(sql)
        cursor = mydb.cursor()
        cursor.execute(sql)
        return 0
    except Exception as e:
        print(e)
        return -1

if __name__ == "__main__":
    connect()
    dbname='sample_db'
    result = create_database(dbname)
    print(result)
        
    connect('localhost','root','1234', dbname)
    table_name = "data"
    fields = '''
          `Name` text,
          `Age` int DEFAULT NULL
    '''    
    result = create_table(table_name, fields)
    print(result)
    #result = reate_table(table_name)

    #result = drop_table(table_name)
    #result = drop_table(table_name)
        
    #result = drop_database(dbname)
    print(result)
    