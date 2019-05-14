def transformstring(x):
    string = str(x)
    return string
    
try:
    fr = open("1.txt", 'r')
    transformstring(fr.name)
    text = fr.readlines()
    print(f"The file contains {len(text)}")
    fr.close()
except:
    print("Zero")