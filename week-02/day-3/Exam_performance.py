"""
    Here is a fictive result of an exam. 
    The examiners have tracked the user id, the result and time spent on the exam. 
    There were no standard time format so each mentor used their own. 
    Now you need to find the user who has got the most points within one min. 
    Your task is to find the highest points/mins ratio within the dataset.
"""



def timetransform(x):
    import re
    title = x[0]
    transformed_content = []
    re_h_extract = r'(\d+)h'
    re_m_extract = r'(\d+)m'
    re_s_extract = r'(\d+)s'
    re_hms_extract = r'(\d+):(\d+):(\d+)'
    p_h = re.compile(re_h_extract)
    p_m = re.compile(re_m_extract)
    p_s = re.compile(re_s_extract)
    p_hms = re.compile(re_hms_extract)
    for i in x[1:]:
        if i[2] != 'null':
            temp = {}
            temp[title[0]] = i[0]
            temp[title[1]] = i[1]
            result_hms = p_hms.search(i[2])
            if result_hms != None:
                temp[title[2]] = float(result_hms.group(1)) * 60 + float(result_hms.group(2)) + float(result_hms.group(3)) / 60
            else:
                result_h = p_h.search(i[2])
                result_m = p_m.search(i[2])
                result_s = p_s.search(i[2])
                if result_h == None:
                    temp_h = 0
                else:
                    if i[2][0] == '.':
                        temp_h = float('0.' + result_h.group(1))
                    else:
                        temp_h = float(result_h.group(1))
                if result_m == None:
                    temp_m = 0
                else:
                    if i[2][0] == '.':
                        temp_m = float('0.' + result_m.group(1))
                    else:
                        temp_m = float(result_m.group(1))
                if result_s == None:
                    temp_s = 0
                else:
                    if i[2][0] == '.':
                        temp_s = float('0.' + result_s.group(1))
                    else:
                        temp_s = float(result_s.group(1))
                temp[title[2]] = temp_h * 60 + temp_m + temp_s / 60         
            transformed_content.append(temp)
    return transformed_content

def exam_maxr(filename):
    try:
        f_exam = open(filename, 'r')
        content = f_exam.read().splitlines()
        for i in  range(len(content)):
            content[i] = content[i].split('\t')
        transformed_content = timetransform(content)
        ratio = {}
        for i in transformed_content:
            ratio[i['user']] = float(i['points']) / i['time']
        sorted_ratio = sorted(ratio.items(), key = lambda x:x[1], reverse = True)
        print(f'the highest points/times ratio is {sorted_ratio[0][1]}')
    except:
        print("Please input a correct filename")
        
exam_maxr('exams.tsv')

