import psycopg2


def get_connection():
    try:
        return psycopg2.connect(
            database="langfuse",
            user="abc",
            password="123",
            host="127.0.0.1",
            port=5432,
        )
    except:
        print("Connection failed")
        return False


conn = get_connection()
if conn:
    print("Connection to the PostgreSQL established successfully.")
else:
    print("Connection to the PostgreSQL encountered and error.")

curr = conn.cursor()
# EXECUTE THE SQL QUERY
curr.execute(" select * from traces where id in (SELECT trace_id FROM scores ORDER BY value desc LIMIT 10) ;")
# FETCH ALL THE ROWS FROM THE CURSOR
data = curr.fetchall()
# PRINT THE RECORDS
for row in data:
    print(row)
# CLOSE THE CONNECTION
conn.close()

def get_top_traces():
    return NotImplementedError
