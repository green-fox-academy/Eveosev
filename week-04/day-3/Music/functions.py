import sys
import psycopg2
import re
con = psycopg2.connect(
    host = '127.0.0.1',
    user = 'postgres',
    password = 'Winds147963!',
    database = 'postgres'
)

cur = con.cursor()

def add_song(str):
    insert_query = 'INSERT INTO music (artist, title) VALUES (%s, %s)'
    regex = r'([\w+\s]+)[\:\,](.+)|artist\s\"(.+\w+).+title\s\"(.*)\"'
    p = re.compile(regex)
    result = p.search(str)
    try:
        name = result.group(1)
        title = result.group(2)
    except:
        name = result.group(3)
        title = result.group(4)
    cur.execute(insert_query, (name, title,))
    con.commit()
    cur.close()
    con.close()


def list_song():
    select_query = 'SELECT * FROM todo'
    cur.execute(select_query)
    data = cur.fetchall()
    cur.close()
    con.close()
    return data    


def remove_song(id:int):
    delete_query = 'DELETE FROM music WHERE id = %s'
    cur.execute(delete_query, id)
    con.commit()
    cur.close()
    con.close()
    return "Delete successfully"


def check_event(id:int):
    check_query = 'SELECT * FROM todo WHERE id = %d'
    cur.execute(check_query, id)
    con.commit()
    cur.close()
    con.close()
    return 