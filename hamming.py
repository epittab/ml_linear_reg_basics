def hamming_distance(pt1, pt2):
  distance = 0
  for point in range(len(pt1)):
    if (pt1[point] != pt2[point]):
      distance += 1
  return distance

print(hamming_distance([1, 2], [1, 100]))
print(hamming_distance([5, 4, 9], [1, 7, 9]))