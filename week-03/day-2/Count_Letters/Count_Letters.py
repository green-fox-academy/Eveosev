def count_letters(str1):
    str1_C_dict = {}
    for letter in str1:
        str1_C_dict[letter] = str1_C_dict.get(letter, 0) + 1
    return str1_C_dict
