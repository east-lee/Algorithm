def dfs(result,used):
    global combination
    if len(result) == n:
        combination.append(result)
        return 0
    for i in range(n):
        r = result[:]
        u = used[:]
        if i in used:
            continue
        else:
            r.append(possible_num[i])
            u.append(i)
            dfs(r,u)




T = int(input())
for t in range(1,T+1):
    n,k=map(int,input().split())
    possible_num = [i for i in range(1,n+1)]
    combination = []
    dfs([],[])

    num = 0

    for i in range(len(combination)):
        for j in range(len(combination)):
            sum_result = 0
            A = combination[i]
            B = combination[j]
            for m in range(n):
                sum_result += max(A[m],B[m])
            if sum_result >= k:
                num +=1
    print(f'#{t} {num}')

