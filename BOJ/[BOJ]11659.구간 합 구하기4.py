def get_data():
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    return [N, M, arr]

def solution():
    sum_arr = [0] * (N)

    for i in range(N):
        sum_arr[i] = sum_arr[i-1] + arr[i] if i > 0 else arr[i]

    return sum_arr

if __name__ == "__main__":
    N, M, arr = get_data()

    sum_arr = solution()
    # print(sum_arr)
    for _ in range(M):
        start_point, end_point = map(int, input().split())
        result = sum_arr[end_point-1] - sum_arr[start_point-2] if start_point >= 2 else sum_arr[end_point-1]
        print(result)

