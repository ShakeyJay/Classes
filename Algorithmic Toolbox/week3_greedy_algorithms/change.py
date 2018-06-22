# Uses python3
import sys

def get_change(m):
    #write your code here
    d,n,p = 10,5,1
    count = 0

    while m != 0:
        if m >= d:
            m -= d
            count += 1
        elif m >= n:
            m -= n
            count += 1
        else:
            m -= p
            count += 1

    return count

if __name__ == '__main__':
    m = int(input())
    print(get_change(m))
