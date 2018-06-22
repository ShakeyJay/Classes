# Uses python3
def calc_fib(n):
    if (n <= 1):
        return n

    return calc_fib(n - 1) + calc_fib(n - 2)




def main():
    n = int(input())
    print(calc_fib(n))

if __name__ == "__main__":
    main()