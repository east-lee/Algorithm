testing = True
while testing:
    arr = input()
    if not arr:
        break
    stack = []
    result = 0
    for i in arr:
        if not stack:
            result += 10
            stack.append(i)
        else:
            if stack[-1] == i:
                stack.append(i)
                result += 5
            else:
                stack.append(i)
                result +=10
    print(result)

