import math
import random
def minimumSwaps(arr):
    length = len(arr)
    total = 0
    hasht = dict()
    for x in range(length):
        hasht.update({arr[x] : x})
    for x in range(length):
        if x+1 != arr[x]:
            arr[hasht[x+1]], hasht[arr[x]]= arr[x], hasht[x+1]
            total += 1
        arr[x] = 0
    return total

arrlen = 10
randomlist = random.sample(range(1, arrlen+1), arrlen)
array = [1, 3, 5, 2, 4, 6, 7]
array2 = [4, 3, 1, 2]
array3 = [1, 3, 2, 7, 6, 5, 4, 8]
arr = [2,1,3,4,5,6,7]
arr1 = [6, 8, 10, 7, 2, 5, 3, 1, 4, 9]
x = arr1
print(x)
print(minimumSwaps(x))