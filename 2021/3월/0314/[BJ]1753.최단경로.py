
v,e = map(int,input().split())
start = int(input())
check = list([0]*(v+1) for _ in range(v+1))
for _ in range(e):
    u,v_e,w = map(int,input().split())
    if check[u][v_e]:
        check[u][v_e] = min(check[u][v_e],w)
    else:
        check[u][v_e] = w

INF = 10**10
result = [INF]*(v+1)
result[start] = 0

for i in range(1,v+1):
    if i == start:
        result[i] = 0
    elif check[start][i]:
        result[i] = check[start][i]

for i in range(1,v+1):
    if i == start:
        continue
    check_i = [INF]*(v+1)
    for j in range(1,v+1):
        if i==j:
            check_i[j] = 0
        elif check[i][j]:
            result[j] = min(result[j],check[i][j]+result[i])
result = result[1:]
for i in result:
    print( i if i!=INF else "INF")
