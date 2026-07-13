def first_non_repeating(s):
    frequency = {}

    for ch in s:
        frequency[ch] = frequency.get(ch, 0) + 1

    for ch in s:
        if frequency[ch] == 1:
            return ch

    return None


text = input("Enter a string: ")

result = first_non_repeating(text)

if result:
    print("First Non-Repeating Character:", result)
else:
    print("No unique character found.")