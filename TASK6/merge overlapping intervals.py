# Program to merge overlapping intervals

intervals = [[1, 3], [2, 4], [5, 7], [6, 8]]
intervals.sort()
merged = [intervals[0]]

for start, end in intervals[1:]:
    last_end = merged[-1][1]
    if start <= last_end:
        merged[-1][1] = max(last_end, end)
    else:
        merged.append([start, end])

print("Merged Intervals:", merged)
