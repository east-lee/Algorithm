import copy

def check(arr,i,j):
    direction = [[-1,0],[1,0],[0,1],[0,-1],[1,1],[-1,1],[1,-1],[-1,-1]]
    arr[i][j] = 1
    for k in range(8):
        y,x = i,j
        while True:
            if 0<=y+direction[k][0]<n and 0<=x+direction[k][1]<n:
                y += direction[k][0]
                x += direction[k][1]
                arr[y][x] = 1
            else:
                break
    return arr


def solution(arr,k,n):
    global result
    if k == n:
        result += 1
        return
    for i in range(n):
        new_arr = copy.deepcopy(arr)
        if new_arr[k][i] == 0:
            new_arr = check(new_arr,k,i)
            solution(new_arr,k+1,n)

def main(n):
    arr = list([0]*n for _ in range(n))
    solution(arr,0,n)

if __name__ == "__main__":
    n = int(input())
    result = 0
    main(n)
    print(result)