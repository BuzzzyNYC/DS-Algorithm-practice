'''
problem analysis:
- n segments with a coordinate [l,r]
- find a segment that covers all other segments --> print the order of the segment
- else print -1

'''

from cmath import inf


n = int(input())
minl = float(inf)
maxr = 0
number = 0
for i in range(1, n + 1):
    l, r = map(int, input().split())
    if l <= minl and r >= maxr:
        number = i
    elif l < minl or r > maxr:
        number = -1
    minl = min(minl, l)
    maxr = max(maxr, r)
print(number)