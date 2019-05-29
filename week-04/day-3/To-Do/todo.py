import psycopg2
import sys

con = psycopg2.connect(
    host = '127.0.0.1',
    user = 'postgres',
    password = 'Winds147963!',
    database = 'todo',
    port = '5432'
)

# print(con.get_dsn_parameters())

#create cursor
cur = con.cursor()

#Call the todo list
def call_todo_list():
    select_query = 'SELECT * FROM todo'
    cur.execute(select_query)
    data = cur.fetchall()
    cur.close()
    con.close()
    return data


#Insert data to table Todo
def add_todo_event(event):
    insert_query = 'INSERT INTO todo (description) VALUES (%s)'
    cur.execute(insert_query, (event,))
    con.commit()
    cur.close()
    con.close()
    return call_todo_list()


#Remove an event from todo_list
def remove_event(id:int):
    delete_query = 'DELETE FROM todo WHERE id = %s'
    cur.execute(delete_query, id)
    con.commit()
    cur.close()
    con.close()
    return call_todo_list()

#Check the to-do event
def check_event(id:int):
    check_query = 'SELECT * FROM todo WHERE id = %d'
    cur.execute(check_query, id)
    con.commit()
    cur.close()
    con.close()
    return call_todo_list()

