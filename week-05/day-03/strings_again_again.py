def strings(string):
    if len(string) > 1:
        if "*"  in string:
            if string[1] == '*':
                return string
            else:
                n = string.find('*')
                new_string = string[:n-1] + "*" + string[n-1:]
                return strings(new_string)
        else:
            n = string.find('*')
            new_string = string[:n] + "*" + string[n:]
            return strings(new_string)
    else:
        return f"Please input a longer string"

print(strings('Thanks, Levi and Steven'))
print(strings('x'))
print(strings('Thx'))


#("*").join(list(string))