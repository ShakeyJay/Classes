#Uses python3

import sys

def largest_number(a):
    #write your code here
    holder = []

    # First Attempt
    # print(a)
    # count = 0
    # holder.append(a[0])
    # for i in range(1,len(a)):
    #     new_split = a[i][0]
    #     # print(new_split)
    #     count += 1
    #     for x in range(len(holder)):
    #         old_split = holder[x][0]
    #         # print(new_split, old_split, count, holder)
    #         if int(new_split) > int(old_split):
    #             holder.insert(x, a[i])
    #             # print('if')
    #             break
    #         elif int(new_split) >= int(holder[x][len(holder[x]) - 1]) and len(holder[x]) > len(a[i]):
    #             holder.insert(x, a[i])
    #             # print('elif')
    #             break
    #     else:
    #         holder.append(a[i])
    #         # print('else')
    # # print(holder, 'hold')


    holder.append(a[0])
    for i in range(1,len(a)):
        for x in range(len(holder)):
            # print(holder[x], a[i])
            if isGreater(holder[x], a[i]):
                holder.insert(x, a[i])
                break
        else:
            holder.append(a[i])
            # print('else')
        # print(holder, 'hold')

    res = "".join(str(e) for e in holder)
    return res


def isGreater(first, second):
    # split_first = list(first)
    # split_second = list(second)

    # print(split_first, 'first')
    # print(split_second, 'second')


    # WOWOWOW
    woo = first + second
    yay = second + first

    # print(woo)
    # print(yay)

    if int(yay) > int(woo):
        return True
    return False


    # if int(split_second[0]) > int(split_first[0]):
    #     print('if')
    #     return True
    # elif int(split_second[0]) == int(split_first[0]):
    #     if int(split_second[len(split_second) - 1]) > int(split_first[len(split_first) - 1]):
    #         print('elifif')
    #         return True
    #     elif len(split_second) < len(split_first):
    #         return True
    #     print('elifelse')
    #     return False
    # print('else')
    # return False

if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))
    

# 452410110 452411010