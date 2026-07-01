arr = [10, 20, 30, 40, 50]

first = arr[0]

for i in range(len(arr) - 1):
    arr[i] = arr[i + 1]

arr[-1] = first

print("Array after Left Rotation:")
print(arr)