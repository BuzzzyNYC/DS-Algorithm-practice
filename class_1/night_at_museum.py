"""
- print letters in a circle, clockwise and counterclockwise.
- static pointer points at "a" but not necessarily all the time.
- find minimum number of rotations needed to print a word
- corner case: need to print 1 letter --> sum = 0
"""
'''
algorithm:
read string s
initialize static pointer = 'a'
initialize sum = 0

pseudo-code:
static_pointer = 'a'
sum = 0
for i in range(len(s))
count_1 = abs(s[i] - start)
count_2 = 26 - count_1
sum += min(count_1, count_2)
update static pointer = s[i]

s = 'ares'
i = 'a'
count_1 = abs(97 - 97)
count_2 = 26 - 0
sum = 0
start = a

i = 'r'
count_1 = abs(114 - 97)=17
count_2 = 26 - 17 = 9
sum = 9
start = 'r'

i = 'e'
count_1 = abs(101 - 114) = 13
count_2 = 26 - 13 = 13
sum = 22
start = 'e'

i = 's'
count_1 = abs(115 - 101) = 14
count_2 = 26 - 14 = 12
sum = 34
start = 's'
'''
s = input("Enter a string: ")
static_pointer = 'a'
sum = 0

for i in range(len(s)):
    count_1 = abs(ord(s[i]) - ord(static_pointer))
    count_2 = 26 - count_1
    sum += min(count_1, count_2)
    static_pointer = s[i]
print(sum)

'''
time complexity: O(n)
space complexity: O(1)
'''