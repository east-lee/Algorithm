from heapq import heappush, heappop

def main():
    start, end = map(int,input().split())
    INF = 10000000000000
    result = [INF]*(N+1)
    result[start] = 0

    heap = []
    heappush(heap,(0,start))
    while heap:
        weight, idx = heappop(heap)
        for e, v in arr[idx]:
            if result[e] > weight + v:
                result[e] = weight + v
                heappush(heap,(weight+v,e))

    print(result[end])

if __name__ == "__main__":
    N,M = list(int(input()) for _ in range(2))

    arr = list([] for _ in range(N+1))
    for _ in range(M):
        s,e,v = map(int,input().split())
        arr[s].append((e,v))

    main()
