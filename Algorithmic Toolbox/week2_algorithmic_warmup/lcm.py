# Uses python3
import sys

def lcm_naive(a, b):
    for l in range(1, a*b + 1):
        if l % a == 0 and l % b == 0:
            return l

    return a*b

def josh_gcd(a,b):
    while min(a,b) > 1:
        a,b = min(a,b), max(a,b) % min(a,b)
    if b == 0:
        return a
    return min(a,b)

def josh_lcm(a,b):
    # If both numbers are even divide them by 2
    gcd = josh_gcd(a,b)
    return (a*b)//gcd

if __name__ == '__main__':
    a, b = map(int, input().split())
    # print(lcm_naive(a, b))
    print(josh_lcm(a,b))

