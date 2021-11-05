def solution():
    global arr
    sorted_arr = arr[:]
    sorted_arr.sort(key=lambda x:-x)
    result = [-1] * N
    visited = [False] * N
    arr_pointer, sorted_arr_pointer = 0, 0
    cnt = 1
    while sorted_arr_pointer != N:
        flag = False
        while not flag:
            if not visited[arr_pointer] and sorted_arr[sorted_arr_pointer] == arr[arr_pointer]:
                visited[arr_pointer] = True
                result[arr_pointer] = cnt
                cnt += 1
                flag = True
                sorted_arr_pointer += 1
            arr_pointer += 1
            arr_pointer %= N

    return result


if __name__ == "__main__":
    TC = int(input())

    for _ in range(TC):
        N, M = map(int, input().split())
        arr = list(map(int, input().split()))
        result = solution()
        print(result[M])