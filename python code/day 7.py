# Problem: Calculate the sum of all digits without converting the number to a string.

# solution


a=1234
total =0
while a>0:
   num= a%10
   total = total + num
   a=a//10
print(total)
