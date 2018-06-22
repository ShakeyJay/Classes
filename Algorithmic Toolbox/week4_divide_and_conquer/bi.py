# Uses python3
import sys
import math


def binary_search(a, x, low, high):
    # left, right = 0, len(a)
    # write your code here
    # med = math.floor(len(a)//2)
    med = math.floor(low + (high-low)/2 )
    # print('med=',med, 'x=', x, 'a=', a, 'high=', high, 'low=', low)
    # find the middle element floor(len(a)//2)
    if high < low or (high == low and high > len(a)-1):
        return -1
    if a[med] == x:
        return med
    elif x < a[med]:
        return binary_search(a, x, low, med-1)
    else:
        return binary_search(a, x, med+1, high)

def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[n + 1]
    a = data[1 : n + 1]
    for x in data[n + 2:]:
        # replace with the call to binary_search when implemented
        print(binary_search(a, x, 0, len(a)), end = ' ')
