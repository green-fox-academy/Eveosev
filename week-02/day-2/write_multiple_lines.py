def modify(path, word, number):
    f = open(path, 'a')
    for i in range(number):
        f.write(word + "\n")
    f.close()

try:
    modify("apple.txt", 'apple', 5)
except:
    pass