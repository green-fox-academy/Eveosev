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
