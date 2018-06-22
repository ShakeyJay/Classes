# Uses python3
from sys import stdin

def fibonacci_sum_squares_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    sum      = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        sum += current * current

    return sum % 10

def get_pisano(n,m=10):
    h = [0, 1]

    for i in range(2, m*m + 1):
        h.append((h[i-2] + h[i-1]) % m)
        if h[i-1] == 0 and h[i] == 1:
            return h[:-2]

def josh_fib_sum(n):
    if n <= 1:
        return n

    h = get_pisano(n,10)
    place = n % len(h)
    
    ld = sum(h[:place+1]) % 10

    if place+1 != len(h):
        return (h[place] * h[place+1]) % 10
    else:
        return (h[place] * h[0]) % 10

    return ld

if __name__ == '__main__':
    n = int(input())
    print(josh_fib_sum(n))
