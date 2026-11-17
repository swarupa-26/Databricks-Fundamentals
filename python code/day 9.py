# Problem: A list contains numbers from 1 to 6, but one number is missing.

arr = [1, 2, 3, 5, 6]

n = 6
expected = 0
actual = 0

for i in range(1, n + 1):
    expected = expected + i

for i in range(len(arr)):
    actual = actual + arr[i]

print(expected - actual)