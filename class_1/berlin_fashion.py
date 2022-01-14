'''
Problem statement:
- a jacket should be fasten by all the buttons except only one.
- Corner case: if a jacket has only one button, that must be fasten
- fasten arr[i] == 1
- not fasten arr[i] == 0
'''
n = int(input())
arr = list(map(int, input().split()))

if n == 1:
    if arr[0] == 1:
        print("YES")
    else:
        print("NO")
else:
    count = 0
    for i in range(n):
        count += arr[i]
    if count == n - 1:
        print("YES")

    else:
        print("NO")

