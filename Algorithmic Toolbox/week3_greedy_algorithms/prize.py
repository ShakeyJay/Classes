# Uses python3
import sys
from random import *

def optimal_summands(n):
    summands = []
    #write your code here
    # while n > 0:
    #     print(n, len(summands), n // 2)
    #     if n // 2 < len(summands):
    #         print('if')
    #         summands[0] += n
    #         n = 0
    #         break
    #     else:
    #         print('else')
    #         n //= 2
    #         summands.append(n)
    # return summands

    # tmp  = 0
    # while (tmp+1) * 2 < n:
    #     if sum(summands) > n // 2:
    #         break
    #     tmp += 1
    #     summands.append(tmp)
    # if len(summands) == 0:
    #     summands.append(n)
    # elif n - sum(summands) > summands[len(summands) - 1]:
    #     summands.append(n - sum(summands))
    # else:
    #     summands[len(summands) - 1] += (n - sum(summands))
    # return summands


    # As long as the last one + 1 < n - (last + 1) we append

    summands.append(1)
    n -= 1

    while summands[len(summands) - 1] < n: #(n - summands[len(summands) - 1]) + 1:
        # print(summands[len(summands) - 1] + 1, n - (summands[len(summands) - 1] + 1))
        summands.append(summands[len(summands) - 1] + 1)
        n -= summands[len(summands) - 1]
        # print('n=', n)
        # print(summands[len(summands) - 1], (n - summands[len(summands) - 1]) + 1, 'end')
    if n > 0:
        summands[len(summands) - 1] += n
    return summands

def test():
    while True:
        # n = randint(1, 100000000)
        n = randint(1, 100)

        res1 = optimal_summands(n)

        if sum(res1) == n and res1[len(res1) - 1] >= n // 2:
            print('Ok')
        else:
            print('Wrong Answer')
            print(res1)
            print(n)
            print(sum(res1[:-1]))
            sys.exit()

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
    # test()
