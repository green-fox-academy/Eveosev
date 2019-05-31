import sys
import psycopg2
import functions

con = psycopg2.connect(
    host = '127.0.0.1',
    user = 'postgres',
    password = 'Winds147963!',
    database = 'postgres'
)

cur = con.cursor()
#Create music table
"""
create_table_query = 'CREATE TABLE music (id SERIAL, artist VARCHAR(50), title VARCHAR(50))'
cur.execute(create_table_query)
con.commit()
"""

key = sys.argv[1]

if key == 'a':
    functions.add_song(sys.argv[2])
elif key == 'd':
    functions.remove_song(sys.argv[2])
elif key == 'p':
    pass
elif key == 'l':
    pass
    

