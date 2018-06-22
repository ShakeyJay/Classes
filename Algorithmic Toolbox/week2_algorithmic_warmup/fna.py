# Uses python3
import sys

def get_fibonacci_huge_naive(n, m):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % m

def get_pisano(n,m):
    h = [0, 1]

    for i in range(2, m*m + 1):
        h.append((h[i-2] + h[i-1]) % m)
        if h[i-1] == 0 and h[i] == 1:
            return h[:-2]

def josh_fib_huge(n,m):
    if n <= 1:
        return n

    holder = get_pisano(n,m)
    print(holder)
    l = len(holder)

    return holder[n % l] 


if __name__ == '__main__':
    n, m = map(int, input().split())
    print(josh_fib_huge(n, m))
