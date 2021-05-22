from collections import deque
# from heapq import heappop, heappush

def main():
    v1_to_v2 = min_route[1][v1] + min_route[v1][v2] + min_route[v2][N]
    if min_route[1][v1] == INF or min_route[v1][v2] == INF or min_route[v2][N] == INF:
        v1_to_v2 = 'not'
    v2_to_v1 = min_route[1][v2] + min_route[v2][v1] + min_route[v1][N]
    if min_route[1][v2] == INF or min_route[v2][v1] == INF or min_route[v1][N] == INF:
        v2_to_v1 = 'not'
    if v1_to_v2 == 'not' and v2_to_v1 == 'not':
        return -1
    if v1_to_v2 == 'not':
        return v2_to_v1
    if v2_to_v1 == 'not':
        return v1_to_v2



    return min(v1_to_v2,v2_to_v1)






def find_min_route(n):
    global min_route

    dq = deque()
    dq.append(n)


    while dq:

        x = dq.popleft()
        check_list = route[x]
        for end,cost in check_list:
            if min_route[x][end] > cost:
                min_route[x][end] = cost
                min_route[end][x] = cost
                dq.append(end)
    # for i in min_route:
    #     print(i)



if __name__ == "__main__":
    N, E = map(int,input().split())
    INF = 10000
    route = [[] for _ in range(N+1)]
    min_route = list([INF]*(N+1) for _ in range(N+1))
    for i in range(N+1): min_route[i][i] = 0

    for _ in range(E):
        a, b, c = map(int,input().split())
        min_route[a][b] = min(min_route[a][b],c)
        min_route[b][a] = min(min_route[b][a],c)
        route[a].append([b,c])
        route[b].append([a,c])

    v1, v2 = map(int,input().split())
    for n in [1,v1,v2]:
        find_min_route(n)
    print(main())
    for i in min_route:
        print(i)