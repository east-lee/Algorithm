def main():
    global rgb, rg, check_rgb, check_rgh

    for i in range(n):
        for j in range(n):
            if not check_rgb[i][j]:
                rgb_solution(i,j,1)
                rgb += 1
            if not check_rg[i][j]:
                rgb_solution(i,j,0)
                rg += 1

def rgb_solution(i,j,normal):
    global check_rgb, check_rg
    if normal: check_list = check_rgb
    else: check_list = check_rg

    check_color = []
    if normal: check_color = [arr[i][j]]
    else:
        if arr[i][j] == "R" or arr[i][j] == "G":
            check_color = ["R","G"]
        else:
            check_color = ['B']
    q = []
    q.append([i,j])
    check_list[i][j] = 1
    while q:
        y,x = q.pop()
        for k in range(4):
            next_y,next_x = y+direction[k][0], x+direction[k][1]
            if 0<=next_y<n and 0<=next_x<n and check_list[next_y][next_x] == 0 and arr[next_y][next_x] in check_color:
                check_list[next_y][next_x] = 1
                q.append([next_y,next_x])

if __name__ == "__main__":
    n = int(input())
    arr = list(input() for _ in range(n))
    direction = [[-1,0],[1,0],[0,-1],[0,1]]
    check_rgb = list([0] * n for _ in range(n))
    check_rg = list([0] * n for _ in range(n))

    rgb = 0
    rg = 0 #적록색약이 아닌사람
    main()
    print(f'{rgb} {rg}')