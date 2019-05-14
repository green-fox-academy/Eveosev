# Create a method that decrypts encoded-lines.txt
def decrypt_encoded(file_name):
    try:
        f = open(file_name, 'r')
        contents = f.readlines()
        decoded_contents = []
        for i in range(len(contents)):
            temp = ''
            for j in range(len(contents[i]) - 2):
                if contents[i][j] == " ":
                    temp = temp + " "
                else:
                    temp = temp + chr(ord(contents[i][j]) - 1)
            decoded_contents.append(temp)
        return decoded_contents
    except:
        print('Error')

decrypt_encoded('encoded-lines.txt')

import re
# Create a method that find the 5 most common lottery numbers in lottery.csv
def five_most_frequent(filename):
    try:
        ft = open(filename, 'r')
        contents = ft.readlines()
        lotterynumbers = []
        regex_lottery = r'(\d+\;\d+\;\d+\;\d+\;\d+)'
        p_lottery = re.compile(regex_lottery)
        for i in contents:
            lotterynumbers.append(p_lottery.search(i).group().split(";"))
        stat = {}
        for i in range(0,100):
            count = 0
            for j in lotterynumbers:
                if str(i) in j:
                    count += 1
            stat[str(i+1)] = count
        ordered_stat = sorted(stat.items(), key = lambda x:x[1], reverse = True)
        for key in  ordered_stat[0:5]:
            print(f"{key}")
    except:
           print("Error") 
five_most_frequent('lottery.csv')
