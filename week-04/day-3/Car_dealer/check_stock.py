import psycopg2
import json

with open('car.json') as car:
    data = json.load(car)

con = psycopg2.connect(
    host = '127.0.0.1',
    user = 'postgres',
    password = 'Winds147963!',
    database = 'postgres'
)

cur = con.cursor()

def check():
    select_query = 'SELECT * FROM car'
    cur.execute(select_query)
    result = cur.fetchall()
    for row in result:
        print(row)

