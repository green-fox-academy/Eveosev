import changeTime
import meanTime
import medianTime
import matplotlib
#The first working day is Jan 14th

with open('logs.csv', 'r') as f:
    result = f.read().splitlines()
import re
"""
door_regex = r'(\(\S+)'
p_finddoor = re.compile(door_regex)
doors = []
missvalue = []
for i in result:
    foundresult = p_finddoor.search(i)
    if foundresult != None:
        doors.append(foundresult.group())
    else:
        missvalue.append(i)
uniquedoors = set(doors)
"""
#Filter the records according different people
date_time_door_ppl = []
regex_pdt = r'\,(.+)\.\s(\S+)\,Ac.+(\(\S+\)).+(\d{5}\:\d+)'
p_pdt = re.compile(regex_pdt)
missing = []
for  row in result:
    matchresult = p_pdt.search(row)
    if matchresult != None:
        date_time_door_ppl.append([matchresult.group(1), matchresult.group(2), 
                                   matchresult.group(3), matchresult.group(4)])
    else:
        missing.append(row)
        
#find the workdays
date = []
for row in date_time_door_ppl:
    date.append(row[0])
uniquedate = list(set(date))
#sort the uniquedate:
#qsort
qsort = lambda arr: len(arr) > 1 and qsort(list(filter(lambda x: x <= arr[0], arr[1:]))) + arr[0:1] + qsort(list(filter(lambda x: x > arr[0], arr[1:]))) or arr
uniquedate = qsort(uniquedate)

stat = {}
for row in date_time_door_ppl:
    stat[row[3]] = stat.get(row[3], {})
for row in date_time_door_ppl:
    if stat[row[3]].get(row[0]) == None:
        stat[row[3]][row[0]] = [[row[1], row[2]]]
    else:
        stat[row[3]][row[0]].append([row[1],row[2]])

#Find and print the average arrvial time
ave_arrivalT = {}
for d in uniquedate:
    temp = []
    for ppl in stat:
        if d in stat[ppl]:
            if stat[ppl][d][0][1] == '(F-1)':
                temp.append(stat[ppl][d][0][0])
    changedTime = changeTime(temp)
    meantime = meanTime(changedTime)
    ave_arrivalT[d] = meantime
 
for key in ave_arrivalT:
    print(f"{key} -- {ave_arrivalT[key]}")

#Find the median of the arrivals
median_arrivalT = {}
day_arrivalT = {}
for d in uniquedate:
    temp = []
    for ppl in stat:
        if d in stat[ppl]:
            if stat[ppl][d][0][1] == '(F-1)':
                temp.append(stat[ppl][d][0][0])
    changedTime = changeTime(temp)
    day_arrivalT[d] = [temp]
    mediantime = medianTime(changedTime)
    median_arrivalT[d] = mediantime

 









