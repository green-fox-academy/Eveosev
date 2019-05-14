"""
    Copy File
"""
def copy(filename):

    try:
        f_original = open(filename, 'r')
        contents = f_original.readlines()
        f_original.close()
        f_copied = open("copied_" + filename, 'a')
        for line in contents:
            f_copied.write(line)
        f_copied.close()
        return True
    except:
        return False

copy("appe.txt")


"""
   Tic_Tax_Toe
"""
import  re

def tic_tac_result(filename):
    regex = r"(\w+)\."
    p = re.compile(regex)
    result = p.search(filename)
    return result.group(1).title()

print(tic_tac_result("win-o.txt"))

print(tic_tac_result("win-x.txt"))

print(tic_tac_result("draw.txt"))

"""
   Logs
"""
fr = open("log.txt", 'r')
logs = fr.readlines()



def uniqueIP(record):
    IP_array = []
    regex_IP = r'(\d+\.\d+\.\d+\.\d+)'
    p_IP = re.compile(regex_IP)
    for i in range(len(record)):
        IP_array.append(re.search(p_IP, record[i]).group())
    unique_IP = set(IP_array)
    return unique_IP
    
uniqueIP(logs)

def ratio(file, string):
    count = 0
    for i  in  file:
        if string in i:
            count += 1
    ratio = count / len(file)
    return ratio

ratio(logs, 'GET')
ratio(logs, 'POST')








