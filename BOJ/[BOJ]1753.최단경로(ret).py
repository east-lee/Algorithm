import heapq

v,e = map(int,input().split())
start = int(input())
check = list([] for _ in range(v+1))
for _ in range(e):
    u,v_e,w = map(int,input().split())
    check[u].append([w,v_e])

INF = 10**10
result = [INF for _ in range(v+1)]
result[start] = 0

q=[]
heapq.heappush(q,[0,start])

while q:
    w,end_point = heapq.heappop(q)
    if result[end_point] < w:
        continue
    for d,x in check[end_point]:
        d += w
        if d<result[x]:
            result[x] = d
            heapq.heappush(q,[d,x])
result = result[1:]
for i in result:
    print (i if i!=INF else "INF")