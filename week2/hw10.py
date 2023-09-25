def contains_repeated_chars(s):
    for i in range(len(s)):
        if s[i] == s[i + 1]:
            j = i + 2
            while j < len(s) and s[j] == s[i]:
                j += 1
            if j - i > 1:
                return True
    return False


print("请输入：")
s = input()
if contains_repeated_chars(s):
    print("Yes")
else:
    print("No")
