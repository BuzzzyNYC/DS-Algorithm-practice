'''
Simplifying problem:
- Given string S and string T equal size
- string S is lexicographically smaller than string T
- Find a string that is as the same size as S and T, and lexicographically 
larger than S and smaller than T.
- Strings are all lowercase letters.
'''

'''
algorithm:
- traverse string s from right to left
- if a character is 'z', change 'z' to 'a'
- else add 1 to the current character and return string
- else: No such string
'''
s = input()
t = input()
for i in range(len(s) - 1, -1, -1):
    if s[i] == 'z':
        s = s[:i] + chr(97) + s[i+1:]
    else:
        a = ord(s[i]) + 1
        s = s[:i] + chr(a) + s[i+1:]
        break
if s < t:
    print(s)
else:
    print("No such string")

# // #include <iostream>
# // #include <string>
# // using namespace std;

# // int main()
# // {
# //     string s, t;
# //     cin >> s >> t;
# //     string c = s;
# //     int n = s.length();
# //     for (int i = n - 1; i >= 0; i--)
# //     {
# //         while (c[i] < 'z')
# //         {
# //             c[i]++;
# //             if (c < t)
# //             {
# //                 cout << c << endl;
# //                 return 0;
# //             }
# //         }
# //         if (c[i] == 'z') {
# //           c[i] = 'a';
# //         }
          
# //     }
# //     cout << "No such string" << endl;
# //     return 0;
# // }




