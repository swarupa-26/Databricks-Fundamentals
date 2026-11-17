# Problem: Find the first element that occurs more than once while scanning from left to right.

# solution

arr = [10, 5, 3, 4, 3, 5, 6]


found = False

for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
        if arr[i] == arr[j]:
            print(arr[i])
            found = True
            break

    if found:
        break

if not found:
    print("No repeating element")
