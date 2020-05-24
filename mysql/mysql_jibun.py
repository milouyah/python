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

def create_database(name,charset='utf8'):
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

def create_table(name, fields=None):
    try:
        if fields == None:
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
    result = create_database('jibun')
    print(result)
        
    connect('localhost','root','1234', 'jibun')
    tablename = "sejong_jibun"

    fields = """        
        관리번호 VARCHAR(25) NOT NULL, 
        일련번호 VARCHAR(3) NOT NULL,
        법정동코드 VARCHAR(10),
        시도명 VARCHAR(20),
        시군구명 VARCHAR(20),
        법정읍면동명 VARCHAR(20),
        법정리명 VARCHAR(20),
        산여부 VARCHAR(1) COMMENT '0:대지, 1:산',
        지번본번_번지 INT DEFAULT 0,
        지번부번_호 INT DEFAULT 0,
        대표여부 VARCHAR(1) COMMENT '0:일반, 1:대표(지번)',
        id INT AUTO_INCREMENT PRIMARY KEY
    """
    create_table(tablename, fields)
    print(result)
    