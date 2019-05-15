"""
    Write a method which can read and parse a file containing information about the door chip usage at the A66.
    The method must return how many times a chip was used at the main door each day 
    (A66 - 04 FÕBEJÁRAT (F-1) Door #1).

    During the development you will need only three fields from the input:

    Date
    Description #1 - the used door
    Card number
"""

def Check2(filename):
    import re
    f_log = open(filename, 'r')
    content = f_log.read().splitlines()
    filter_door = []
    regex_door = r'(\d{4}\.\d{2}\.\d{2}).+(F\-1).+(\d{5}\:\d{5})'
    p_door = re.compile(regex_door)
    empty = []
    for i in content:
        result = p_door.search(i)
        if result != None:
            filter_door.append([result.group(3), result.group(1)])
        else:
            empty.append(i)
    users = []
    for i in filter_door:
        users.append(i[0])
    users = list(set(users))
    dates = []
    for i in filter_door:
        dates.append(i[1])
    dates = list(set(dates))
    stat = {}
    for i in users:
        temp_list = []
        for j in dates:
            count = 0
            temp = {}
            for k in filter_door:
                if i in k and j in k:
                    count += 1
            if count != 0:
                temp[j] = count
                temp_list.append(temp)
        stat[i] = temp_list
        import json
        f_log_json = open('logsresult.json', 'w')
        json.dump(stat, f_log_json, indent = 0)
        f_log_json.write("\n")
        f_log_json.close()
    return stat
         
stat = Check('logs.csv')

#This is a very amazing skill learnt from Claire!!!!!!!!!!!
def secCheck2(filename):
    import re
    f_log = open(filename, 'r')
    content = f_log.read().splitlines()
    filter_door = []
    regex_door = r'(\d{4}\.\d{2}\.\d{2}).+(F\-1).+(\d{5}\:\d{5})'
    p_door = re.compile(regex_door)
    empty = []
    for i in content:
        result = p_door.search(i)
        if result != None:
            filter_door.append([result.group(3), result.group(1)])
        else:
            empty.append(i)
    stat2 = {}
    for i in filter_door:
        stat2[i[0]] = stat2.get(i[0], {})
        stat2[i[0]][i[1]] = stat2[i[0]].get(i[1], 0) + 1
    return stat2
secCheck2('logs.csv')