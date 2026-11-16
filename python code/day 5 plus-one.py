# problem statement : https://leetcode.com/problems/plus-one/description/?envType=problem-list-v2&envId=array

# solution:

a="".join(str(i) for i in l)
b=int(a)+1
ans=[int(i) for i in str(b)]
print(ans)

# print(type(a))
