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

def create_database(name):
    try:
        sql = f"CREATE DATABASE {name}"
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

def create_table(name):
    try:
        fields = "name VARCHAR(255), address VARCHAR(255)"
        sql = f"CREATE TABLE {name} ({fields})"
        print(sql)
        cursor = mydb.cursor()
        cursor.execute(sql)
        return 0
    except Exception as e:
        print(e)
        return -1
    
    
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
    result = create_database('moving_averate')
    print(result)
        
    connect('localhost','root','1234', 'moving_average')
    dbname = "sasung_electronics"
    create_table(dbname)
    create_table(dbname)
    drop_table(dbname)
    drop_table(dbname)
        
    result = drop_database('moving_averate')
    print(result)
    