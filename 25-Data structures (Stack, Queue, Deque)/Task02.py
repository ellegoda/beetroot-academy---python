def are_brackets_balanced(sequence):
    stack = []
    opening_brackets = {'(', '[', '{'}
    closing_brackets = {')': '(', ']': '[', '}': '{'}

    for char in sequence:
        if char in opening_brackets:
            stack.append(char)
        elif char in closing_brackets:
            if not stack or stack.pop() != closing_brackets[char]:
                return False

    return not stack


input_sequence = input("Enter a sequence of characters: ")
if are_brackets_balanced(input_sequence):
    print("Brackets are balanced.")
else:
    print("Brackets are not balanced.")