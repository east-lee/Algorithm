def main():
    result = [100000] * (N+1)
    check = [0]*(N+1)
    p = start
    check[p] = 1
    result[p] = 0
    q = bus_info[p]
    for i in q:
        result[i] = min(result[i],cost_arr[p][i])
    new_q = []
    while q:
        p = q.pop()
        if not check[p]:
            check[p] = 1
            for i in bus_info[p]:
                result[i] = min(result[i],result[p]+cost_arr[p][i])
                new_q.append(i)
        if not q and new_q:
            q = new_q[::-1]
            new_q = []
    print(result[end])

if __name__ == "__main__":
    N,M = (int(input()) for _ in range(2))
    bus_info = [[] for _ in range(N+1)]
    cost_arr = list([100000]*(N+1) for _ in range(N+1))
    for _ in range(M):
        s,e,v = list(map(int,input().split()))
        bus_info[s].append(e)
        cost_arr[s][e] = min(cost_arr[s][e],v)

    start, end = map(int,input().split())
    main()

