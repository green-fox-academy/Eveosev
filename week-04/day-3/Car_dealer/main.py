import psycopg2
import json

with open('car.json') as car:
    data = json.load(car)

print(data)
