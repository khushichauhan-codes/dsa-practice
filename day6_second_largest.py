arr = [10, 50, 20, 80, 60]

largest = second = float('-inf')

for num in arr:

    if num > largest:
        second = largest
        largest = num

    elif num > second and num != largest:
        second = num

print("Second Largest:", second)