def solution(x):
    global check,cnt
    q = []
    q.append(x)
    while q:
        p = q.pop()
        for i in range(1,n+1):
            if (arr[i][p] or arr[p][i]) and not check[i]:
                check[i] = cnt
                q.append(i)
                arr[i][p] = 0
                arr[p][i] = 0
n,m = map(int,input().split())
arr = list([0]*(n+1) for _ in range(n+1))

for _ in range(m):
    u,v = map(int,input().split())
    arr[u][v] = 1
    arr[v][u] = 1

check = [0]*(n+1)
cnt = 0
for i in range(1,n+1):
    if not check[i]:
        cnt += 1
        check[i] = cnt
        solution(i)
print(cnt)