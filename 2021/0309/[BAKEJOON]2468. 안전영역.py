def main(n,h):
    check = []
    for i in range(n):
        check_append = [0]*n
        for j in range(n):
            if arr[i][j] <= h:
                check_append[j] = 0
            else:
                check_append[j] = 1
        check.append(check_append)
    return solution(n,check)

def solution(n,check):
    cnt = 0
    for i in range(n):
        for j in range(n):
            if check[i][j]:
                cnt += 1
                check = check_related(i,j,check)
    return cnt

def check_related(y,x,check):
    q=[[y,x]]
    while q:
        i,j=q.pop()
        for k in range(4):
            ni, nj = i+direction[k][0], j+direction[k][1]
            if 0<=ni<len(check) and 0<=nj<len(check) and check[ni][nj]:
                check[ni][nj] = 0
                q.append([ni,nj])
    return check



direction = [[-1,0],[1,0],[0,-1],[0,1]]
if __name__ == "__main__":
    n = int(input())
    arr = list(list(map(int,input().split())) for _ in range(n))
    max_height = []
    min_height = []
    for i in range(n):
        max_height.append(max(arr[i]))
        min_height.append(min(arr[i]))
    max_height = max(max_height)
    min_height = min(min_height)
    if min_height == max_height:
        result = 1
        print(result)
    else:
        max_result = 0
        for i in range(min_height,max_height):
            result = main(n,i)
            if result > max_result: max_result = result
        print(max_result)