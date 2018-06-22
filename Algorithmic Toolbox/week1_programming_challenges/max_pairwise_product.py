# python3

from random import *

def max_pairwise_product(numbers):
    n = len(numbers)
    max_product = 0
    for first in range(n):
        for second in range(first + 1, n):
            max_product = max(max_product,
                              numbers[first] * numbers[second])

    return max_product


def josh_max_pairwise_product(numbers):
    n = len(numbers)
    high = 0
    next_high = 0
    for first in range(n):
        if numbers[first] > high:
            next_high = high
            high = numbers[first]
        elif numbers[first] > next_high:
            next_high = numbers[first]
    return high * next_high
            
def test():
    array = []
    while True:
        n = randint(2,10)
        for _ in range(1,n):
            array.append(randint(0, 10000))
            # array[i] = randint(0, 10)
        print(array)
        res1 = max_pairwise_product(array)
        res2 = josh_max_pairwise_product(array)
        if res1 == res2:
            print('OK')
            array = []
        else:
            print('Wrong Answer', res1, res2)
            return

if __name__ == '__main__':
    # test()

    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    # print(max_pairwise_product(input_numbers))
    print(josh_max_pairwise_product(input_numbers))


