'''
Problem analysis:
- the game lasts 90 mins
- if 15 consecutive minutes are boring --> TV off
- calculate how many minutes Bear watched the game

input: 
line 1: n = number of interesting minutes
line 2: n integers t1, t2, ... in increasing order seperated with a space

algorithm:
- we find the difference between each element of the array
- if the first element is greater than 15 --> the answer is right away 15
- else: if the difference is less or equal than 15 then add the difference to the sum of minutes watched
- if the current index is equal to array[-1]--> print 90
9
15 30 45 60 75 90
'''
n = int(input())
arr = list(map(int, input().split()))
min_index = 0
min_watch = 0
for i in range(n):
    if (arr[i] - min_index) > 15:
        if i == 0:
            min_watch += 15
        else:
            min_watch = min_index + 15
        break
    else:
        if i == n - 1:
            if (arr[i] + 15) >= 90:
                min_watch = 90
            else:
                min_watch = arr[i] + 15
        else:
            min_watch = arr[i]
    min_index = arr[i]
print(min_watch)
    

