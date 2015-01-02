"""
To find closest pair of points amongst given set of points in a geometric plane.
"""
import math


def read_input(filename):
    """
    read input from file and return set of points.
    """
    points = []
    infile = open(filename, 'r')
    for line in infile.readlines():
        coords = line.split(',')
        x = int(coords[0].strip())
        y = int(coords[1].strip())
        points.append((x, y))
    return points


def merge_sort(list_num, coord):
    """
    merge sort function to sort points by a coordinate(x/y): O(nlogn)
    """
    if len(list_num) == 1:
        return [list_num[0]]

    first_half = list_num[:len(list_num) / 2]
    second_half = list_num[len(list_num) / 2:]
    first_half = merge_sort(first_half, coord)
    second_half = merge_sort(second_half, coord)

    i, j = 0, 0
    result = []
    while i < len(first_half) and j < len(second_half):
        if first_half[i][coord] < second_half[j][coord]:
            result.append(first_half[i])
            i += 1
        elif first_half[i][coord] > second_half[j][coord]:
            result.append(second_half[j])
            j += 1
        else:
            # if sorting coord is equal, sort by the other coord.
            if first_half[i][coord - 1] < second_half[j][coord - 1]:
                result.append(first_half[i])
                i += 1
            else:
                result.append(second_half[j])
                j += 1

    while i < len(first_half):
        result.append(first_half[i])
        i += 1
    while j < len(second_half):
        result.append(second_half[j])
        j += 1

    return result


def euclidean_distance(point1, point2):
    """
    utility function to calculate the euclidean distance between pair of points.
    """
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)


def closest_split_pair(p_x, p_y, delta):
    """
    for the unlucky case when pair is split across both regions.
    take a vertical strip of width delta on both sides of x bar.
    linear scan through strip sorted by y, considering atmost 7 neighbours.
    """
    s_y = []
    x_bar = p_x[len(p_x) / 2 - 1][0]
    for point in p_y:
        if (float(x_bar) - delta) < point[0] < (float(x_bar) + delta):
            s_y.append(point)

    best_pair = None, None
    best_distance = delta

    for i in range(len(s_y) - 1):
        for j in range(1, min(7, len(s_y) - i)):
            if euclidean_distance(s_y[i], s_y[i + j]) < best_distance:
                best_distance = euclidean_distance(s_y[i], s_y[i + j])
                best_pair = s_y[i], s_y[i + j]
    if best_distance < delta:
        print "Closest Split Pair: Best Distance for", best_pair, "is", best_distance  # if split pair found.
    return best_pair


def closest_pair(p_x, p_y):
    """
    Divide and Conquer method to find the closest pair given a list of candidate points.
    """
    # base case, 3 points
    if len(p_x) == 3:
        return (p_x[0], p_x[1]) if euclidean_distance(p_x[0], p_x[1]) < euclidean_distance(p_x[1], p_x[2]) else (p_x[1], p_x[2])
    # base case, 2 points
    if len(p_x) == 2:
        return (p_x[0], p_x[1])

    q_x = p_x[:len(p_x) / 2]
    r_x = p_x[len(p_x) / 2:]

    # print q_x, '\t', r_x

    x_bar = q_x[-1][0]  # x value of the rightmost point in the left region.
    y_bar = q_x[-1][1]  # y value of the rightmost point in the left region, own mod.

    q_y = []
    r_y = []

    for point in p_y:
        if point[0] > x_bar:
            r_y.append(point)
        elif point[0] < x_bar:
            q_y.append(point)
        else:
            # dilemma case.
            if point[1] > y_bar:
                r_y.append(point)
            else:
                q_y.append(point)
    # lucky cases.
    p1, q1 = closest_pair(q_x, q_y)
    p2, q2 = closest_pair(r_x, r_y)

    if euclidean_distance(p1, q1) < euclidean_distance(p2, q2):
        better_pair = p1, q1
    else:
        better_pair = p2, q2
    delta = euclidean_distance(better_pair[0], better_pair[1])

    # split pair
    ps, qs = closest_split_pair(p_x, p_y, delta)

    if ps is None and qs is None:  # Lucky Case
        return better_pair
    else:
        return ps, qs


def main():
    """
    main function.
    """
    points = read_input('Points Input.txt')
    print points
    p_x = merge_sort(points, 0)
    p_y = merge_sort(points, 1)
    p, q = closest_pair(p_x, p_y)
    print "Closest pair of points are", p, "and", q

if __name__ == "__main__":
    main()
