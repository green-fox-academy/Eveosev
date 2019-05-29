import psycopg2

#connect to db
con = psycopg2.connect(
    host = '127.0.0.1',
    database = 'postgres',
    user = 'postgres',
    password = 'Winds147963!',
    port = '5432'
)

print(con.get_dsn_parameters())

#cursor
cur = con.cursor()


cur.execute("SELECT * FROM movie")


# row = cur.fetchall()
# print(type(row))
# for i in row:
#     print(i)

insert_query = 'INSERT INTO movie VALUES (%s, %s, %s, %s)'
mid = 102
title = '123'
year = 123
director = '123'
cur.execute(select_query)
# cur.mogrify(select_query, (mid, title, year, director))
#cursor.execute(insert_query, {
#   'mid': mid
#   'title': title
#   'year': year
#   'director: director'})

#After inserting , we need commit
con.commit()



#Conditional search
select_query = ''

row = cur.fetchall()
print(type(row))
for i in row:
    print(i)

print(cur.rowcount)  #print how many rows you change




#clost the connection

cur.close()
con.close()
