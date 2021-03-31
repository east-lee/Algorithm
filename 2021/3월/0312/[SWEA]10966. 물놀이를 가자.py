def main():
    n, m = map(int, input().split())
    arr = list(input() for _ in range(n))
    check = list([n*m]*m for _ in range(n))
    water_place = []
    new_place = []
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 'W':
                water_place.append([i,j,0])
                check[i][j] = 0
    cnt = 1
    while water_place:
        y,x,length = water_place.pop()
        for k in range(4):
            i,j = y+direction[k][0],x+direction[k][1]
            if 0<=i<n and 0<=j<m and length+1 < check[i][j]:
                check[i][j] = length+1
                new_place.append([i,j,length+1])
        if not water_place and new_place:
            cnt += 1
            water_place = new_place
            new_place = []

    result = 0
    for i in check:
        result += sum(i)

    return result

direction = [[-1,0],[1,0],[0,-1],[0,1]]
if __name__ == "__main__":
    T = int(input())
    for t in range(1,T+1):
        print(f'#{t} {main()}')