# below is used to generate a large list to compare the two functions, which one is faster
# from random import sample
# list = sample(range(100,100000000),50000000) 
list = [11,35,47,20,60,89,73,105,99]
list.sort()
target = int(input('Enter an integer: '))

# low efficient search:

def search(target):
    if target not in list:
        return str(target) + ' is not in the list.'
    for i in list:
        if i == target:
            return str(target) + ' is in list and index is: ' + str(list.index(target))
    


# Binary Search
def binarySearch(list,target):
    # lowerbound lb and higherbound hb,middle mid in a sorted list
    lb = 0  # list[lb] = list[0] will be the first (lowest) element
    hb = len(list)-1  # list[len(list)-1] last, highest element
    while lb <= hb:
        mid = (lb+hb)//2

        if target == list[mid]:
            return str(target) + ' is in the list with index ' + str(mid)
        elif target>list[mid]:
            lb = mid + 1
        else:           #target < list[mid]
            hb = mid - 1

    return str(target) + ' is not in the list.'


# try a list with 100000000 elements(random) and see  the speed difference.
