#####
# Linear Search Code taken from:
# https://www.geeksforgeeks.org/linear-search/
import random
# Binary Search Code taken from:
# https://www.geeksforgeeks.org/binary-search/


# on 01/17/2023
# License: Share-alike
# https://www.geeksforgeeks.org/copyright-information/?ref=footer
# ChangeLog:
# Combine driver code into one
# Refactor code
# Change the array data to random array
# Add counter to count operation for individual algorithms
# Add timer code to time individual algorithms
#####

# Python3 code to linearly search x in arr[].
# If x is present then return its location,
# otherwise return -1
import timeit
from random import Random


def search(arr, n, x):
    operations = 0
    for i in range(0, n):
        operations += 1
        if arr[i] == x:
            return i
    return -1


# Python3 code to implement iterative Binary
# Search.

# It returns location of x in given array arr
# if present, else returns -1
def binarySearch(arr, l, r, x):
    operations = 0
    while l <= r:
        operations += 1
        mid = l + (r - l) // 2
        # Check if x is present at mid
        if arr[mid] == x:
            return mid

        # If x is greater, ignore left half
        elif arr[mid] < x:
            l = mid + 1

        # If x is smaller, ignore right half
        else:
            r = mid - 1

    # If we reach here, then the element
    # was not present
    return -1


# Driver Code
if __name__ == "__main__":
    # arr = [2, 3, 4, 10, 40]
    arr = random.sample(range(200), 200)
    x = 10
    n = len(arr)
    import timeit
    iter = 10
    ltime = timeit.timeit(lambda: search(arr, n, x),\
                          setup="from __main__ import binarySearch", number=iter)
    btime = timeit.timeit(lambda: binarySearch(arr, 0, len(arr) - 1, x),\
                          setup="from __main__ import binarySearch", number=iter)
    print("Linear search took:", ltime)
    print("Binary search took:", btime)

    # Function call
    result = search(arr, n, x)
    if result == -1:
        print("Element is not present in array")
    else:
        print("Element is present at index", result)

# Driver Code
# arr = [2, 3, 4, 10, 40]
random.sample(range(200), 200)
x = 10

# Function call
result = binarySearch(arr, 0, len(arr) - 1, x)

if result != -1:
    print("Element is present at index % d" % result)
else:
    print("Element is not present in array")
