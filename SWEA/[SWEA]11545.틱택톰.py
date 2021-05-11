def solution(i,j):
    k = []
    if not i:
        k.append(0)
    if not i and not j:
        k.append(2)
    if not j:
        k.append(1)
    if not i and j == 3:
        k.append(3)
    if arr[i][j] =='.':
        k = []
    return k




direction = [[1,0],[0,1],[1,1],[1,-1]]
T = int(input())
for t in range(1,T+1):
    if t>1:
        blank = input()
    arr = list(input() for _ in range(4))


    completed = True
    winner = False

    for i in range(4):
        for j in range(4):
            range_direction = solution(i,j)
            if arr[i][j] == '.': completed = False
            #print(range_direction)
            for k in range_direction:
                cnt = 0
                save_record = []
                y, x = i,j

                while cnt < 4:
                    if arr[y][x] == '.':
                        break
                    save_record.append(arr[y][x])
                    y += direction[k][0]
                    x += direction[k][1]
                    cnt += 1
                    if 0>x or 0>y or x>=4 or y>=4:
                        break

                if len(save_record) != 4:
                    continue

                if 'O' in save_record and 'T' in save_record and 'X' not in save_record:
                    winner = 'O'
                elif 'O' in save_record and 'X' not in save_record:
                    winner = 'O'
                elif 'X' in save_record and 'T' in save_record and 'O' not in save_record:
                    winner = 'X'
                elif 'X' in save_record and 'O' not in save_record:
                    winner = 'X'
            if winner:
                break
        if winner: break

    if completed and not winner:
        print(f'#{t} Draw')
    elif not completed and not winner:
        print(f'#{t} Game has not completed')
    elif winner:
        print(f'#{t} {winner} won')

