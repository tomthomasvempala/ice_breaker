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


def get_top_traces(connection, limit):
    if connection:
        print("Connection to the PostgreSQL established successfully.")
    else:
        print("Connection to the PostgreSQL encountered and error.")

    curr = connection.cursor()
    # curr.execute(
    #     f" SELECT input from traces where id in (SELECT trace_id FROM scores ORDER BY value desc LIMIT {limit}) ;")
    curr.execute(
        f" SELECT input, s.value from traces t left join scores s on t.id = s.trace_id where t.id in (SELECT trace_id FROM scores ORDER BY value desc LIMIT {limit}) order by s.value desc ;")
    return curr.fetchall()


if __name__ == "__main__":
    connection = get_connection()
    prompts = get_top_traces(connection=connection, limit=3)
    print(len(prompts))
    for prompt in prompts:
        print(prompt[0].get('question'),end=' ')
        print(prompt[1])
    connection.close()
