# O(n log n)
def selection_sort(arr):
    for i in range(len(arr) - 1):
        nxt_min = i
        for j in range(i+1, len(arr)):
            if arr[nxt_min] > arr[j]:
                nxt_min = j
        arr[i], arr[nxt_min] = arr[nxt_min], arr[i]

    return arr


def selection_sort2(arr):
    for i in range(len(arr) - 1):
        rem_arr = arr[i+1:]
        nxt_min = min(rem_arr)
        nm_idx = rem_arr.index(nxt_min) + i + 1
        if nxt_min < arr[i]:
            arr[i], arr[nm_idx] = arr[nm_idx], arr[i]

    return arr

def bubble_sort(arr):
    # Your code here
    disorder = True
    while disorder:
        disorder = False
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i +1] = arr[i +1], arr[i]
                disorder = True
    return arr

'''
STRETCH: implement the Counting Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
'''

def counting_sort(arr, maximum=None):
    if len(arr) == 0:
        return arr
    if maximum == None:
        maximum = max(arr) + 1
    buckets = [0] * maximum
    for i in arr:
        if i < 0:
            return 'Error, negative numbers not allowed in Count Sort'
        buckets[i] += 1
    arr = []
    for i in range(len(buckets)):
        arr += [i] * buckets[i]
    return arr
