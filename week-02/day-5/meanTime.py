def meanTime(timeset):
    meantime = ""
    sum_h = 0
    sum_m = 0
    sum_s = 0
    for row in timeset:
        sum_h += int(row[0])
        sum_m += int(row[1])
        sum_s += int(row[2])
    TotalTinSec = sum_h * 3600 + sum_m * 60 + sum_s
    mean = TotalTinSec / len(timeset)
    mean_h = int(mean // 3600)
    mean_m = int((mean - mean_h * 3600 ) // 60)
    mean_s = int((mean - mean_h * 3600 - mean_m * 60))
    meantime = str(mean_h) + ":" + str(mean_m) + ":" + str(mean_s)
    return meantime
