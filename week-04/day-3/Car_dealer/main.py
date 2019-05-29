import psycopg2
import json
import check_stock
import datetime

with open('car.json') as car:
    data = json.load(car)

con = psycopg2.connect(
    host = '127.0.0.1',
    user = 'postgres',
    password = 'Winds147963!',
    database = 'postgres'
)

cur = con.cursor()

#Create table car
create_table_query = 'CREATE TABLE car (id INT, brand VARCHAR(50), model VARCHAR(50), year INT, condition VARCHAR(50), price INT, count INT);'
cur.execute(create_table_query)
con.commit()


#Migrate
insert_query = 'INSERT INTO car VALUES (%s, %s, %s, %s, %s, %s, %s)'
for i in data:
    cur.execute(insert_query, list(i.values()))
    con.commit()


#Check the Table car
check_stock.check()


#Remove cars that are not in stock
remove_query = 'DELETE FROM car WHERE count = 0'
cur.execute(remove_query)
con.commit()
check_stock.check()


#Reduce price
update_query = 'UPDATE car SET price = price * 0.8'
cur.execute(update_query)
con.commit()
check_stock.check()


#Count the average age of car in stock
total_car_num_query = 'SELECT SUM(count) FROM car'
cur.execute(total_car_num_query)
total_car_num = cur.fetchall()[0][0]

total_car_year_query = 'SELECT SUM(year * count) FROM car'
cur.execute(total_car_year_query)
total_car_year = cur.fetchall()[0][0]

total_car_age = datetime.datetime.now().year * total_car_num - total_car_year 
average_car_age = total_car_age / total_car_num
print(average_car_age)

#Do it in SQL:
"""
SELECT ((SELECT SUM(year * count) FROM car) - EXTRACT(year from  NOW()) * (SELECT SUM(count) FROM car)) / (SELECT SUM(count) FROM car);
"""
#Close
cur.close()
con.close()