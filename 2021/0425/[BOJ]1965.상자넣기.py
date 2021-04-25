def main():
    dp = [1]*(n+1)
    dp[0]=0
    for i in range(1,n+1):
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i]=max(dp[j]+1,dp[i])
    print(max(dp))


if __name__ == "__main__":
    n = int(input())
    arr = list(map(int,input().split()))
    arr.insert(0,0)
    main()