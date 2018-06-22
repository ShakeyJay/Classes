# python3


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
    return high * next_high
            


if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    # print(max_pairwise_product(input_numbers))
    print(josh_max_pairwise_product(input_numbers))


