#Insertion sort
original_insertion = [4, 1, 3, 2, 8]
def insertion(array):
    n = len(array)
    for i in range(1, n):
        for j in range(i , 0 , -1):
            if array[j] < array[j-1]: 
                array[j],array[j-1]=array[j-1],array[j]
            else:
                break
    return array
insertion(original_insertion)
