def rotate_array(arr, k):
    n = len(arr)
    k = k % n
    return arr[-k:] + arr[:-k]

arr = list(map(int, input("Enter array elements: ").split()))
k = int(input("Enter k: "))

print("Rotated Array:", rotate_array(arr, k))