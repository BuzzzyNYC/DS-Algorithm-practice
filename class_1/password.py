'''
problem analysis:
- Vanya has a list of n passwords for his website, but he doesn't
remember which password is for which website
- therefore, he will enter those passwords in order of non-decreasing 
their lengths, and he will enter passwords of same length in arbitrary order.
- it takes one second to enter a password, but if he gets the password wrong k times (k <=100),
he will have to wait another 5 seconds to enter another password.
- Determine how many seconds will Vanya need to enter the right password in the best case 
and in the worst case.
'''


n, k = map(int, input().split())
arr = []
for i in range(n):
    s = input()
    arr.append(s)
password = input()
smaller = same = 0
for i in range(n):
    if len(arr[i]) < len(password):
        smaller += 1
    if len(arr[i]) == len(password) and arr[i] != password:
        same += 1
        
wrong_attempt_best = smaller
wrong_attempt_worst = smaller + same
delay_best = wrong_attempt_best // k
delay_worst = wrong_attempt_worst // k

print(wrong_attempt_best + delay_best * 5 + 1, wrong_attempt_worst + delay_worst * 5 + 1) 