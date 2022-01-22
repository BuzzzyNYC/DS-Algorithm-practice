'''
Problem analysis:
- You are given an array arr consists of n integers. 
- Find a minimal by inclusion substring [l,r] (1 <=l<=r<=n) such, that it has
exactly k distinct numbers.
'''
n, k = map(int, input().split())
a = list(map(int, input().split()))
count = [0]* (100000+1)
unique = 0

for i in range(0, n-1):
    if count[a[i]] == 0:
        unique += 1
    count[a[i]] += 1
    if unique == k:
        j = 0
        while True:
            if count[a[j]] > 1:
                count[a[j]] -= 1
                j += 1
            else:
                print(j+1, i+1)
                exit()
print("-1 -1")