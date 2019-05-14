f = open("my-file.txt", 'r')

try:
    f.write("Peiwen Wu")
except:
    print("Unable to write file: my-file.txt")

