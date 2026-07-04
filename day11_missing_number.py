n = int(input("Enter value of n: "))
arr = list(map(int, input("Enter numbers: ").split()))

total = n * (n + 1) // 2
missing = total - sum(arr)

print("Missing Number:", missing)