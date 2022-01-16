'''
- arrays A and B
- choose K numbers in A and M numbers
in B so that any number chosen in A is 
less than any chosen number in B
- return YES or NO
'''
'''
algorithm:
we compare the 
size A = 3 size B = 3
K = 2 M = 1
A = 1 2 3
B = 3 4 5
'''
a, b = map(int, input().split())
k, m = map(int, input().split())

list_a = list(map(int, input().split()))
list_b = list(map(int, input().split()))
print(list_b[b-m])
print(list_b[b-1-m])
if list_a[k-1] < list_b[b-m]:
    print("YES")
else:
    print("NO")
