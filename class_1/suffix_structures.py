'''
Problem analysis:
- given two distinct words, s and t
- we need to transfrom word s into word t using 2 techniques:
automaton, array
- automaton: remove from this string any single character.
- array: swap any two characters of this string
- any structure may be used an unlimited number of times, the structures may be used in any order.

input: 
- s > 0
- t > 0
- s != t
output:
- print 'need tree' if cannot transform s into t
- print 'automaton' if transform s into t using automaton data structure
- print 'array' if using array 
- print 'both' if transform s into t using both automaton and array
'''

s = input()
t = input()
cnt_s = [0]*26
cnt_t = [0]*26
for i in range(len(s)):
    cnt_s[ord(s[i]) - ord('a')] += 1
for i in range(len(t)):
    cnt_t[ord(t[i]) - ord('a')] += 1
need_tree = automaton = array = False
# case 1,2
for i in range(26):
    if cnt_t[i] > cnt_s[i]:
        need_tree = True
    else:
        if cnt_t[i] < cnt_s[i]:
            automaton = True
# case 3
match = -1
for i in range(len(t)-1):
    id = s[match+1: len(s)-1].find(t[i])
    if id != -1:
        match = id
    else:
        array = True
if need_tree:
    print("need tree")
elif automaton and array:
    print("both")
elif automaton:
    print("automaton")
else:
    print("array")