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
        return False


def get_top_traces(connection,limit):
    if connection:
        print("Connection to the PostgreSQL established successfully.")
    else:
        print("Connection to the PostgreSQL encountered and error.")

    curr = connection.cursor()
    curr.execute(f" SELECT * from traces where id in (SELECT trace_id FROM scores ORDER BY value desc LIMIT {limit}) ;")
    return curr.fetchall()


if __name__ == "__main__":
    connection = get_connection()
    traces = get_top_traces(connection=connection,limit=2)
    print(len(traces))
    print(traces)
    connection.close()
