"""
    Doubled
"""

# Create a method that decrypts the duplicated-chars.txt

def decrypt_doubled(file_name):
    f = open(file_name, 'r')
    contents = f.readlines()
    new_contents = []
    for j in range(len(contents)):
        temp =  ""
        i = 0
        while i < len(contents[j]) - 2:
            temp = temp + contents[j][i]
            i = i + 2
        new_contents.append(temp)
    return new_contents
        
decrypt_doubled('duplicated-chars.txt')



# Create a method that decrypts reversed-lines.txt

def decrypt_reversed(file_name):
    f = open(file_name, 'r')
    contents = f.readlines()
    new_contents = []
    for i in range(len(contents)):
        new_contents.append(contents[i][:-1][::-1])
    return new_contents
        
decrypt_reversed('reversed-lines.txt')

# Create a method that decrypts reversed-order.txt
def decrypt_rordered(file_name):
    f = open(file_name, 'r')
    contents = f.readlines()
    n = len(contents)
    if n % 2 == 0:
        for i in range(n // 2):
            contents[i], contents[n-i-1] = contents[n-i-1], contents[i]
    else:
         for i in range((n-1) // 2):
            contents[i], contents[n-i-1] = contents[n-i-1], contents[i]
    return contents


decrypt_rordered('reversed-order.txt')
