def maxinum_finder(arr):
    if len(arr) == 1:
        return arr[0]
    else:
        if arr[0] < arr[1]:
            return maxinum_finder(arr[1:])
        else:
            return maxinum_finder([arr[0]] + arr[2:])

print(maxinum_finder([2,1,5,4,3]))