# Uses python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):
    points = []
    #write your code here
    # First Attempt
    # if the min is > the min in the holder
    # and if the min is < the max then we skip because its covered
    # Likewise we can check is the max is < max of holder and max > min of holder
    # Then it is covered. Never check the middle numbers.
    # else the holder array gets appended with the new segment
    # tmp = 0
    # for s in segments:
    #     print(s, tmp)
    #     tmp += 1
    #     if points == []:
    #         points.append([s.start, s.end])
    #         continue

    #     for count in range(len(points)):
    #         # print(s.start, s.end, points[count][0], points[count][1])
    #         if s.start >= points[count][0] and s.start <= points[count][1]:
    #             # print('skip')
    #             points[count][0] = s.start
    #             break
    #         elif s.end <= points[count][1] and s.end >= points[count][0]:
    #             # print('skip2')
    #             points[count][1] = s.end
    #             break
    #     else:
    #         # print('Add')
    #         points.append([s.start, s.end])

    #     points.sort(key=lambda points: points[0])
    # return points

    # Second Attempt Sort the Segments by the high check if next one in it
    # if it is then skip else add to list.

    segments.sort(key=lambda segments: segments[1])

    for s in segments:
        if points == []:
            points.append(s.end)
            continue

        for count in range(len(points)):
            if s.start <= points[count]:
                break
        else:
            points.append(s.end)
    return points

    

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    for p in points:
        print(p, end=' ')
