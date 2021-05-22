from heapq import heappush, heappop


def main():
    result_1 = arr1[v1] + arr2[v2] + arr3[N]
    result_2 = arr1[v2] + arr3[v1] + arr2[N]
    if arr1[v1] == INF or arr2[v2] == INF or arr3[N] == INF:
        result_1 = 'not'
    if arr1[v2] == INF or arr3[v1] == INF or arr2[N] == INF:
        result_2 = 'not'

    if result_1 == 'not' and result_2 == 'not':
        return -1
    if result_1 == 'not': return result_2
    if result_2 == 'not': return result_1
    return min(result_1,result_2)


def find_min_route(n):

    arr = [INF]*(N+1)
    q= []
    heappush(q,[0,n])
    arr[n] = 0
    while q:
        cost, end = heappop(q)
        for new_cost, new_end in check[end]:
            new_cost += cost
            if new_cost < arr[new_end]:
                arr[new_end] = new_cost
                heappush(q,[new_cost,new_end])
    # print(arr)

    return arr



if __name__ == "__main__":
    N, E = map(int,input().split())
    check = list([] for _ in range(N+1))
    INF = 10000
    for _ in range(E):
        a,b,c = map(int,input().split())
        check[a].append([c,b])
        check[b].append([c,a])
    v1,v2 = map(int,input().split())

    arr1 = find_min_route(1)
    arr2 = find_min_route(v1)
    arr3 = find_min_route(v2)
    print(main())