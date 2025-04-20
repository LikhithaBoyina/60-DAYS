def ValidParentheses(str):
    stack = []
    Parentheses_Mapping = {")":"(","]":"[","}":"{"}

    for i in str:
        if i in Parentheses_Mapping:
            if stack and stack[-1] == Parentheses_Mapping[i]:
                stack.pop()
            else:
                return False
        else:
            stack.append(i)
    return not stack

str = input()
print(ValidParentheses(str))
    