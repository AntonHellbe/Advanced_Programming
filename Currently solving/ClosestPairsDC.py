import sys
import math


lines = [line.rstrip("\n") for line in sys.stdin]

def getCorrectYvalues(x, d, s_y):
    instrip = list()
    for point in s_y:
        if point[0] > (x - d) and point[0] < (x + d):
            instrip.append(point)

    return instrip


def solve_bruteforce(coordinate_list):
    if(len(coordinate_list) == 1):
        return "INFINITY"
    distances = list()
    for i in range(len(coordinate_list)):
        for j in range(len(coordinate_list)):
            if i == j:
                continue
            else:
                x_d = coordinate_list[i][0] - coordinate_list[j][0]
                y_d = coordinate_list[i][1] - coordinate_list[j][1]
                distances.append(math.sqrt(math.pow(x_d, 2) + math.pow(y_d, 2)))

    # print(distances)
    if(len(distances) == 1):
        return distances[0]
    else:
        return min(distances)

def closestPair(pointlist):

    s_x = sorted(pointlist, key=lambda item: item[0])
    s_y = sorted(pointlist, key=lambda item: item[1])
    return solveClosestPairs(s_x, s_y)


def solveClosestPairs(s_x, s_y):
    if len(s_x) <= 3:
        return solve_bruteforce(s_x)

    mid_index = len(s_x) // 2
    x = s_x[mid_index][0]
    points_left  = solveClosestPairs(s_x[:mid_index], s_y)
    points_right = solveClosestPairs(s_x[mid_index:], s_y)
    d = min(points_left, points_right)
    newStrip = getCorrectYvalues(x, d, s_y)
    # print(s_x)
    for i in range(len(newStrip)):
        for j in range(len(newStrip)):
            if i == j:
                continue
            x_d = newStrip[i][0] - newStrip[j][0]
            y_d = newStrip[i][1] - newStrip[j][1]
            if y_d < d:
                temp = math.sqrt(math.pow(x_d, 2) + math.pow(y_d, 2))
                if temp < d:
                    d = temp
    # print(d)
    return d


current_line = 0

while(True):
    no_points = int(lines[current_line])

    if(no_points == 0):
        break

    current_line += 1

    points_list = list()

    for i in range(no_points):
        data = list(map(float, lines[current_line].split()))
        points_list.append((data[0], data[1]))
        current_line += 1

    d = closestPair(points_list)
    print(d)
    # print(closestPair(points_list))