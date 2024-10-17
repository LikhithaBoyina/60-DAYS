def is_valid(s):
    # Dictionary to map closing brackets to their corresponding opening brackets
    bracket_map = {')': '(', '}': '{', ']': '['}
    
    # Stack to keep track of opening brackets
    stack = []
    
    # Iterate over each character in the string
    for char in s:
        # If it's a closing bracket, check if it matches the top of the stack
        if char in bracket_map:
            # Pop from stack if it's not empty, otherwise use a dummy value
            top_element = stack.pop() if stack else '#'
            
            # Check if the top element matches the corresponding opening bracket
            if bracket_map[char] != top_element:
                return False
        else:
            # If it's an opening bracket, push it onto the stack
            stack.append(char)
    
    # If the stack is empty, all brackets were matched correctly
    return not stack

# Input field
s = input("Enter a String : ")
print(is_valid(s))
