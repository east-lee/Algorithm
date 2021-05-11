for _ in range(20):
    n = int(input())
    arr = list(input().split())
    stack = []
    for i in arr:
        try:
            i = int(i)
            stack.append(i)
            
        except:
            last_result = 0
            b = stack.pop()
            a = stack.pop()


            if i =='+':
                last_result = a+b
            if i =='-':
                last_result = a-b
            if i =='*':
                last_result = a*b
            if i =='/':
                last_result = a/b
            stack.append(int(last_result))
    for i in stack: print(i)
            
    

            
            