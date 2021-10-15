def solution(num_a, num_b):
    dp= [0] * D
    dp[0] = K
    dp[1], dp[2] = num_b, num_a
    idx = 3
    while idx < D:
        dp[idx] = dp[idx-2] - dp[idx-1]
        if dp[idx] > dp[idx-1]:
            return False
        idx += 1
    print(dp[-1])
    print(dp[-2])
    return True

def get_data():
    D, K = map(int, input().split())

    return [D, K]

if __name__ == "__main__":
    D, K = get_data()

    for i in range(1, K):
        first_num, second_num = i, K - i
        if first_num >= second_num: break

        if solution(first_num, second_num):
            break

