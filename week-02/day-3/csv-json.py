"""
    Transform users.csv into json and save it.
"""

import json
f_users = open("users.csv", 'r')
f_users_json = open("users_h.json", 'w')
content = f_users.read().splitlines()
for i in range(len(content)):
    content[i] = content[i].split(',')
title = content[0]
n_title = len(title)
jsondata = []
for i in content[1:]:
    temp = {}
    for j in range(n_title):
        temp[title[j]] = i[j]
    jsondata.append(temp)
for i in jsondata:
    json.dump(i, f_users_json)
    f_users_json.write("\n")
f_users_json.close()
f_users.close()


#Using packages
"""
import csv
import json

f_csv = open('users.csv', 'r')
f_json = open('users.json', 'w')

fieldnames = ("id", "first_name", "last_name", "email", "gender", "ip_address")
reader = csv.DictReader(f_csv, fieldnames)
for row in reader:
    json.dump(row, f_json)
    f_json.write('\n')
"""