def isAnagram(s, t):
    if len(s) != len(t):
        return False
    else:
        for i in s:
            if s.count(i) != t.count(i):
                return False
                break
    return True
t = input()
s = input()
print(isAnagram(s,t))
        