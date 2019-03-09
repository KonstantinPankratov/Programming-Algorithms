def search(entries, item):
    low = 0
    high = len(entries) - 1
    attempts = 0
    while low <= high:
        mid = (low + high) // 2
        needed = entries[mid][0]
        attempts = attempts + 1
        if needed == item:
            return [entries[mid][1], attempts]
        if needed > item:
            high = mid - 1
        else:
            low = mid + 1
    return [None, 0]


entries = [
    (1, "Entry 1"),
    (2, "Entry 2"),
    (3, "Entry 3"),
    (4, "Entry 4"),
    (5, "Entry 5"),
    (6, "Entry 6"),
    (7, "Entry 7"),
    (8, "Entry 8"),
    (9, "Entry 9"),
    (10, "Entry 10"),
]

result = search(entries, 8)

print("Searched value:", result[0])
print("Attempts:", result[1])
