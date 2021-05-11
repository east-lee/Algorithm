for _ in range(10):
    n = int(input())
    stack = []
    arr = list(input() for _ in range(n))
    for i in arr:
        if len(i)>=3:
            stack.append(i[2:])
        elif i == 'c':
            print(len(stack))
        else:
            if not stack:
                print('empty')
            else:
                out = stack.pop()
                print(out)

