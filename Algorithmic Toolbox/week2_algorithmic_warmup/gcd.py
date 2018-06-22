# Uses python3
import sys

def gcd_naive(a, b):
    current_gcd = 1
    for d in range(2, min(a, b) + 1):
        if a % d == 0 and b % d == 0:
            if d > current_gcd:
                current_gcd = d

    return current_gcd


def josh_gcd(a,b):
    while min(a,b) > 1:
        a,b = min(a,b), max(a,b) % min(a,b)
    if b == 0:
        return a
    return min(a,b)


if __name__ == "__main__":
    # input = sys.stdin.read()
    a, b = map(int, input().split())
    # print(gcd_naive(a, b))
    print(josh_gcd(a,b))
