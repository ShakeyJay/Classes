# Uses python3
import sys

def fibonacci_partial_sum_naive(from_, to):
    sum = 0

    current = 0
    next  = 1

    for i in range(to + 1):
        if i >= from_:
            sum += current

        current, next = next, current + next

    return sum % 10


def get_pisano(n,m=10):
    h = [0, 1]

    for i in range(2, m*m + 1):
        h.append((h[i-2] + h[i-1]) % m)
        if h[i-1] == 0 and h[i] == 1:
            return h[:-2]

def josh_fib_sum(n,m):
    # if m <= 1:
    #     return n

    h = get_pisano(n,10)
    place = m % len(h)
    place2 = n % len(h)

    # print(h)
    # print(place, m, len(h), place2)
    
    ld = sum(h[place2:place+1]) % 10

    return ld


if __name__ == '__main__':
    from_, to = map(int, input().split())
    print(josh_fib_sum(from_, to))