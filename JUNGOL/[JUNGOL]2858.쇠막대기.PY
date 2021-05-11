testing = True
while testing:
    data = list(input())

    if not data:break
    result = 0
    stick_cnt = 0
    stack = []

    for idx,i in enumerate(data):
        if i =='(':
            stack.append(i)
        elif data[idx-1]=='(' and data[idx]==')':
            stack.pop()
            result+=len(stack)
        else:
            stack.pop()
            result +=1
        

    print(result)
