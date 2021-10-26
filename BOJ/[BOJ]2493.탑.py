def get_data():
    N = int(input())
    tower = list(map(int, input().split()))

    return [N, tower]

if __name__ == "__main__":
    N, tower = get_data()
    result = [0] * (N)
    stack = []

    for i in range(N):
        tower_height = tower[i]

        while stack:
            last_height, last_idx = stack[-1]
            if last_height > tower_height:
                result[i] = last_idx + 1
                break
            else:
                stack.pop()
        stack.append([tower_height, i])

    for r in result:
        print(r,end = " ")
