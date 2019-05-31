import json
import csv
import xml.etree.ElementTree as ET
import psycopg2


#Extract information from json.file
with open('employees.json') as j_file:
    j_data = json.load(j_file)

#Extract information from csv.file
with open('employees.csv') as c_file:
    c_data = list(csv.reader(c_file))

#Extract information from xml.file
tree = ET.parse('employees.xml')
root = tree.getroot()
xml_data = []

for j in range(len(root)):
    temp = {}
    for i in range(len(root[0])):
        temp[root[j][i].tag] = root[j][i].text
    xml_data.append(temp)

#Change the date type and separate the name
import datetime
for row in c_data[1:]:
    row[3] = datetime.datetime.strptime(row[3], '%m/%d/%Y').strftime('%Y/%m/%d')

for subdict in j_data:
    subdict['birth_date'] = datetime.datetime.strptime(subdict['birth_date'], '%d-%b-%Y').strftime('%Y/%m/%d')
    subdict['firstname'] = subdict['name'].split(' ')[0]
    subdict['lastname'] = subdict['name'].split(' ')[1]
    del subdict['name']

for subdict in xml_data:
    subdict['firstname'] = subdict['name'].split(' ')[0]
    subdict['lastname'] = subdict['name'].split(' ')[1]
    del subdict['name']

csv_data_json = []
for row in c_data[1:]:
    temp = {}
    for i in range(len(c_data[0])):
        temp[c_data[0][i]] = row[i]
    csv_data_json.append(temp)


con = psycopg2.connect(
    host = '127.0.0.1',
    user = 'postgres',
    password = 'Winds147963!',
    database = 'postgres'
)

cur = con.cursor()

# insert_csv_query = 'INSERT INTO csvdata VALUES (%s, %s, %s, %s, %s, %s)'
# for row in csv_data_json:
#     cur.execute(insert_csv_query, (row['id'], row['first_name'], row['last_name'], row['gender'], row['birth_date'], row['monthly_salary'],))
#     con.commit()


# insert_json_query = 'INSERT INTO jsondata VALUES (%s, %s, %s, %s, %s, %s, %s, %s)'
# for row in j_data:
#     cur.execute(insert_json_query, (row['id'], row['firstname'], row['lastname'], row['gender'], row['birth_date'], row['monthly_salary'], row['nationality'], row['university'],))
#     con.commit()

# insert_xml_query = 'INSERT INTO xmldata VALUES (%s, %s, %s, %s, %s, %s, %s, %s)'
# for row in xml_data:
#     cur.execute(insert_xml_query, (row['birth_date'], row['branch'], row['firstname'], row['gender'], row['id'], row['lastname'], row['position'], row['salary_by_year'],))
#     con.commit()

