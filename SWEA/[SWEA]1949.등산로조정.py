def main(arr,n,k):
    start_point = []
    max_height = 0
    for i in range(n):
        for j in range(n):
            if max_height < arr[i][j]:
                start_point = []
                start_point.append([i,j])
                max_height = arr[i][j]
            elif max_height == arr[i][j]:
                start_point.append([i,j])
    for i,j in start_point:
        check = list([0]*n for _ in range(n))
        check[i][j] = 1
        solution(i,j,1,1,k, max_height,n,check)





def solution(y,x,result,can_do, k , last_height,n,check):
    global max_result
    for m in range(4):
        new_check = copy_check(n,check)
        next_y,next_x = y+direction[m][0], x+direction[m][1]
        if 0<=next_y<n and 0<=next_x<n and not new_check[next_y][next_x]:
            if arr[next_y][next_x] < last_height:
                new_check[next_y][next_x] = 1
                solution(next_y,next_x,result + 1, can_do,k,arr[next_y][next_x],n,new_check)
            elif arr[next_y][next_x] >= last_height and can_do and last_height > arr[next_y][next_x]-k:
                new_check[next_y][next_x] = 1
                num_check = arr[next_y][next_x]
                cnt = 1
                while cnt <= k:
                    if num_check - cnt < last_height:
                        break
                    cnt += 1

                solution(next_y,next_x,result+1, 0, k, num_check-cnt , n,new_check)
            else:
                if result > max_result:
                    max_result = result
        else:
            if result > max_result:
                max_result = result


def copy_check(n,check):
    new_check = list([0]*n for _ in range(n))
    for i in range(n):
        for j in range(n):
            new_check[i][j] = check[i][j]
    return new_check




direction = [[-1,0],[1,0],[0,-1],[0,1]]

if __name__ == "__main__":
    T = int(input())
    for t in range(1,T+1):
        max_result = 0
        n,k = map(int,input().split())
        arr = list(list(map(int,input().split())) for _ in range(n))
        main(arr,n,k)
        print(f'#{t} {max_result}')