def IsPalindrome(str):
    result = ""
    for char in str.lower():
        if char.isalnum():
            result+=char
    print(result)
    print(result[::-1])
    if result[::-1] == result:
        return True
    else:
        return False
    
str = input()
print(IsPalindrome(str))
