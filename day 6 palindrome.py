# problem statement : https://leetcode.com/problems/palindrome-number/description/


# solution:

x=121
a=list(str(x))
print("a", a)
b=a[::-1]
print("b", b)
if b==a:
   print(True)
else:
    print(False)