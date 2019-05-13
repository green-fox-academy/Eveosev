"""
    Sorting Algorithm
"""

#Bubble sort
original_bubble = [5, 1, 4, 2, 8]
def bubble(array):
    for j in range(len(array) - 1): 
        for i in range(len(array) - 1):
            if array[i] > array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
    return array
bubble(original_bubble)

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

#Quick sort
original_quick = [4, 1, 3, 2, 8]
def quicksort(array):
    if len(array) >= 2:
        left = []
        right = []
        value = array[len(array) // 2]
        array.remove(value)
        for i in array:
            if i > value:
                right.append(i)
            else:
                left.append(i)
        return quicksort(left) + [value] + quicksort(right)
    else:
        return array
quicksort(original_quick)

#Merge sort
def mergesort():
    
    
#Heapsort
    



























