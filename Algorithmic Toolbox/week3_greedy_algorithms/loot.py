# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
    value = 0.
    # write your code here
    total = []
    for i in range(len(weights)):
        total.append([values[i]/weights[i],i])

    total.sort(key=lambda total: total[0], reverse=True)

    while capacity != 0:
        if not total:
            break
        if weights[total[0][1]] <= capacity:
            value += values[total[0][1]]
            capacity -= weights[total[0][1]]
            del total[0]
        else:
            left = capacity / weights[total[0][1]]
            value += values[total[0][1]] * left
            capacity = 0
            del total[0]
    return value  

if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
