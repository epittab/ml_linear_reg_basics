def manhattan_distance(pt1, pt2):
    distance = 0
    for point in range(len(pt1)):
        distance += abs(pt1[point] - pt2[point])
    return distance

print(manhattan_distance([1, 2], [3, 4]))
print(manhattan_distance([5, 3, 1], [2, 9, 7]))
print(manhattan_distance([1, 2, 9], [5, 3, 2]))