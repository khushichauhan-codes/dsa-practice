arr = [10, 20, 30, 40, 50, 60, 70]

target = 60

low = 0
high = len(arr) - 1

while low <= high:

    mid = (low + high) // 2

    if arr[mid] == target:
        print("Element Found at Index", mid)
        break

    elif arr[mid] < target:
        low = mid + 1

    else:
        high = mid - 1

else:
    print("Element Not Found")