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
