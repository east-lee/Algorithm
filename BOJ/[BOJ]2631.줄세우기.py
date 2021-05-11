if __name__ == "__main__":
    N = int(input())
    arr = []
    for _ in range(N): arr.append(int(input()))

    dp = [1]*N

    max_cnt = 0
    for i in range(1,N):
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i],dp[j]+1)
    print(N-max(dp))
