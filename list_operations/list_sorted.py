listA = [2, 15, 30, -20, 74, -100]

print(sorted(listA)) # prints the lowest number first, then ascends

print(sorted(listA, key=int, reverse=True)) # prints the highest number first, then descends