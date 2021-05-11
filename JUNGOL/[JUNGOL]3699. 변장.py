def dfs(k,wearing):
    global result
    if k == N:
        if len(wearing) >=1:
            result += 1
        return 0
    current_wearing = wearing[:]
    item_name = arrs[k][1]
    if item_name in current_wearing:
        dfs(k+1,current_wearing)
    else:
        current_wearing.append(item_name)
        dfs(k+1,current_wearing)
        current_wearing.pop()
        dfs(k+1,current_wearing)



TC = int(input())
for t in range(1,TC+1):
    N = int(input())
    arrs = list(list(map(str,input().split())) for _ in range(N))
    wearing = []
    result = 0
    dfs(0,wearing)
    print(result)
