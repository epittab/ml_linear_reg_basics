import math

def euclidean_distance(pt1, pt2):
    # set dist to 0
    distance = 0
    # take the difference of each pair, square and add them together
    for point in range(len(pt1)):
        num = pt1[point] - pt2[point]
        distance += num ** 2
    # return square root
    return math.sqrt(distance)
    
print(euclidean_distance([1, 2], [3, 4]))
print(euclidean_distance([5, 3, 1], [2, 9, 7]))
print(euclidean_distance([1, 2, 9], [5, 3, 2]))
