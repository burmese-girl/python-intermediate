from collections import Counter
numbers = [1, 1, 5, 2, 3, 5, 2,1, 4]
counts = Counter(numbers)
print(counts)
print(counts.most_common(2))

