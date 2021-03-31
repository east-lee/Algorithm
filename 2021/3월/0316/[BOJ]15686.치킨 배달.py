def solution(check):
    global print_result
    total_result = 0
    for i in home:
        min_result = 10**5
        for j in check:
            result = abs(i[0]-chicken[j][0]) + abs(i[1]-chicken[j][1])
            if result < min_result:
                min_result = result
        total_result += min_result

    if print_result > total_result: print_result = total_result

def chicken_select(check, k,path):
    if k == M:
        solution(path)
        return
    for i in range(len(check)):
        if not check[i] and (not path or path[-1] > i):
            check[i] = 1
            path.append(i)
            chicken_select(check,k+1,path)
            path.pop()
            check[i] = 0


def main():
    chicken_check = [0] * len(chicken)
    chicken_select(chicken_check,0,[])


if __name__ == "__main__":
    N, M = map(int,input().split())
    arr = list(list(map(int,input().split())) for _ in range(N))
    chicken = []
    home = []

    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1: home.append([i,j])
            elif arr[i][j] == 2: chicken.append([i,j])
    print_result = 10**5
    main()

    print(print_result)



