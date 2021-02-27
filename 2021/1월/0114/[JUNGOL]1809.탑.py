testing = True
while testing:
    n = int(input())
    if not n: break
    arr = list(map(int,input().split()))

    stack = [[arr[0],1]]
    max_check = arr[0]
    result = [0]
    for i in range(1,n):
        if arr[i] > max_check:
            max_check=arr[i]
            result.append(0)
            stack = []
        else:
            for j in range(len(stack)-1,-1,-1):
                if stack[j][0] > arr[i]:
                    result.append(stack[j][1])
                    break
        stack.append([arr[i], i + 1])


    for i in result: print(i,end=' ')
    print()

