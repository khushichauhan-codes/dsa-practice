def is_valid(s):
    stack = []

    pairs = {
        ')': '(',
        '}': '{',
        ']': '['
    }

    for ch in s:
        if ch in "([{":
            stack.append(ch)
        else:
            if not stack:
                return False

            top = stack.pop()

            if top != pairs[ch]:
                return False

    return len(stack) == 0


string = input("Enter parentheses: ")

if is_valid(string):
    print("Valid")
else:
    print("Invalid")