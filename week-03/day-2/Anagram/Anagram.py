def Anagram(str1, str2):
    str1_letter_dict = {}
    for i in str1:
        str1_letter_dict[i] = str1_letter_dict.get(i, 0) + 1

    str2_letter_dict = {}
    for i in str2:
        str2_letter_dict[i] = str2_letter_dict.get(i, 0) + 1

    if len(list(str1_letter_dict.keys())) == len(list(str2_letter_dict.keys())):
        for key in str1_letter_dict:
            if key not in str2_letter_dict or str1_letter_dict[key] != str2_letter_dict[key]:
                return False
        return True
    else:
        return False

"""
Easy way in python:
def Anagram(str1, str2):
    list_str1 = list(str1)
    list_str2 = list(str2)
     return sorted(list_str1) == sorted(list_str2)

Difference between sort() and sorted()

1) sort() is a built-in function of list, the usage of it is "list.sort()".
In this case, "list.sort()" returns None.

2) sorted() is a built-in function, the usage of it is "sorted(list)".
In this case, "sorted(list)" returns the sorted list.
"""