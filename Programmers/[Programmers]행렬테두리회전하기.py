def solution(rows, columns, queries):
    answer = []
    
    matrix = [[0]*columns for _ in range(rows)]
    cnt = 0
    for i in range(rows):
        for j in range(columns):
            cnt += 1
            matrix[i][j] = cnt
    
    for x1,y1,x2,y2 in queries:
        matrix,min_num = rotate_matrix(matrix,x1,y1,x2,y2)
        answer.append(min_num)
    
    
    return answer


def rotate_matrix(matrix, y1,x1,y2,x2):
    direction = [[0,1],[1,0],[0,-1],[-1,0]]
    last_num = 100*100+1
    now_num = -1
    
    min_num = 100*100+1
    
    start_y, start_x = y1-1, x1-2
    length_1, length_2 = (x2-x1), (y2-y1)
    
    k = 0
    cnt = -1
    while k<4:
        start_y += direction[k][0]
        start_x += direction[k][1]
        
        now_num = matrix[start_y][start_x]
        matrix[start_y][start_x] = last_num
        last_num = now_num
        cnt += 1
        
        min_num = min(min_num,last_num)
        
        if not k % 2 and cnt == length_1:
            cnt = 0
            k += 1
        elif k % 2 and cnt == length_2:
            cnt = 0
            k += 1
    return [matrix,min_num]
    