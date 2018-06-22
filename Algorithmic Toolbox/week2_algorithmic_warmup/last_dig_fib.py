# Uses python3
import sys

def get_fibonacci_last_digit_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % 10


def josh_last_digit(n):
    if n <= 1:
        return n

    prev = 0
    current = 1

    for _ in range(2, n+1):
        prev, current = current % 10, (prev + current) % 10

    return current

if __name__ == '__main__':
    n = int(input())
    # print(get_fibonacci_last_digit_naive(n))
    print(josh_last_digit(n))
