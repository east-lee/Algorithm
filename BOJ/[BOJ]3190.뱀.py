def main():
    global arr
    cnt = 0
    snake = [[0,0]]
    d = 0
    while True:
        cnt += 1
        next_y,next_x = snake[-1][0]+direction[d][0], snake[-1][1] + direction[d][1]
        if 0<=next_y<n and 0<=next_x<n:
            if [next_y, next_x] in snake:
                break
            if not arr[next_y][next_x]:
                snake.pop(0)
            arr[next_y][next_x] = 0
            snake.append([next_y, next_x])

        else:
            break

        if direction_change and cnt == direction_change[0][0]:
            if direction_change[0][1] == "D":
                d += 1
            else:
                d -= 1
            if d>3:
                d = 0
            elif d<0: d=3
            direction_change.pop(0)
    return cnt



if __name__ == "__main__":
    n,k = int(input()), int(input())
    direction = [[0, 1], [1, 0], [0, -1], [-1, 0]] # D 이면 d+=1 아니면 d-=1
    arr = list([0]*n for _ in range(n))
    for _ in range(k):
        y, x = map(int,input().split())
        arr[y-1][x-1] = 1

    direction_change = []
    for _ in range(int(input())):
        sec, change_direction = map(str,input().split())
        direction_change.append([int(sec),change_direction])

    print(main())

