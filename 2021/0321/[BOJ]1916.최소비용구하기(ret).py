def main():
    start, end = map(int,input().split())
    INF = 100000000000
    result = [INF]*(N+1)
    result[start] = 0

    q =[(0,start)]
    new_q = []
    while q:
        weight, idx = q.pop()
        for e, v in arr[idx]:
            if result[e] > weight + v:
                result[e] = weight + v
                new_q.append((weight+v,e))
        if not q and new_q:
            q = new_q
            new_q = []

    print(result[end])

if __name__ == "__main__":
    N,M = list(int(input()) for _ in range(2))

    arr = list([] for _ in range(N+1))
    for _ in range(M):
        s,e,v = map(int,input().split())
        arr[s].append((e,v))

    main()
