arr = [23, 56, 12, 89, 34, 7]

maximum = arr[0]
minimum = arr[0]

for num in arr:
    if num > maximum:
        maximum = num

    if num < minimum:
        minimum = num

print("Maximum Element:", maximum)
print("Minimum Element:", minimum)