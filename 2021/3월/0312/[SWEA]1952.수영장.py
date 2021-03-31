def main(price,plan):
    dp = [0]*16
    dp_3 = [0]*17
    dp_3[3] = price[2]
    for i in range(1,13):
        dp[i] = dp[i-1] + min(price[0]*plan[i],price[1])
        if i>=3:
            dp[i] = min(dp[i],dp_3[i])
        dp_3[i + 3] = dp[i] + price[2]
    if dp[12]>price[3]:
        return price[3]
    else:
        return dp[12]

if __name__ == "__main__":
    T = int(input())
    for t in range(1,T+1):
        price, plan = list(map(int,input().split())), list(map(int,input().split()))
        plan.insert(0,0)
        print(f'#{t} {main(price,plan)}')

