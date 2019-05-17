def changeTime(timeset):
    Time_in_Separation = []
    for row in timeset:
        temp = row.split(":")
        Time_in_Separation.append(temp)
    return(Time_in_Separation)