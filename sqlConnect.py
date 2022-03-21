import psycopg2
def sendToSql(Date, TransactionID):
    hostname = 'localhost'
    database = 'test'
    username = 'postgres'
    pwd = 'pass'
    port_id = 5432
     
    try:
        conn = psycopg2.connect(
                    host = hostname,
                    dbname = database,
                    user = username,
                    password = pwd,
                    port = port_id) 
        cur = conn.cursor()
        insert_script = 'INSERT INTO transactions (date, transactions) VALUES (%s, %s)'
        insert_value = (Date, TransactionID)
        cur.execute(insert_script, insert_value)
        conn.commit()

        conn.close()
    except Exception as error:
        print(error)
    finally:
        if cur is not None:
            cur.close()
        if conn is not None:
            conn.close()
def getFromSql():
    hostname = 'localhost'
    database = 'test'
    username = 'postgres'
    pwd = 'pass'
    port_id = 5432
     
    try:
        conn = psycopg2.connect(
                    host = hostname,
                    dbname = database,
                    user = username,
                    password = pwd,
                    port = port_id) 
        cur = conn.cursor()
        cur.execute("SELECT * FROM transactions")
        row = cur.fetchone()
        while row is not None:
            return(row[1])

        cur.close()
    except Exception as error:
        print(error)
    finally:
        if cur is not None:
            cur.close()
        if conn is not None:
            conn.close()