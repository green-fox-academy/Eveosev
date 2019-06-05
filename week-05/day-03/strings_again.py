def strings(string):
    if 'x' in string:
        temp = list(string)
        temp[string.find('x')] = ''
        changed_string = "".join(temp)
        return strings(changed_string)
    else:
        return string

print(strings('xyxadsfx'))


#string.replace('x', '')