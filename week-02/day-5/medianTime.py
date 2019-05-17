# -*- coding: utf-8 -*-

def medianTime(timeset):
    mediantime = ""
    temp_time = []
    for row in  timeset:
        h = row[0] * 3600
        m = row[1] * 60
        timeinSec = h + m + row[2]
        temp_time.append(timeinSec)
    temp_time.sort()
    n = len(temp_time)
    if n % 2 != 0:
        mediantime = temp_time[(n + 1) // 2]
    else:
        mediantime = (temp_time[n // 2] + temp_time[n // 2 + 1]) // 2
    mediantime_h = mediantime // 3600
    mediantime_m = (mediantime - mediantime_h * 3600) // 60
    mediantime_s = mediantime - mediantime_h * 3600 - mediantime_m * 60
    Mediantime = str(mediantime_h) + ":" + str(mediantime_m) + ":" + str(mediantime_s)
    return Mediantime