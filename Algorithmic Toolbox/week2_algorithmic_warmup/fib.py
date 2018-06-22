# Uses python3
def calc_fib(n):
    if (n <= 1):
        return n

    return calc_fib(n - 1) + calc_fib(n - 2)

def josh_fib(n):
    if (n <= 1):
        return n
    
    prev = 0
    current = 1
    for _ in range(2,n+1):
        prev, current = current, current + prev
        # tmp = current + prev
        # prev = current
        # current = tmp

    return current


def main():
    n = int(input())
    # print(calc_fib(n))
    print(josh_fib(n))

if __name__ == "__main__":
    main()