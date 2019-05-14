try:
    fr = open("my-file.txt", 'r')
    text = fr.readlines()
    print(text)
except:
    print("Unable to read file: my-file.txt")
    