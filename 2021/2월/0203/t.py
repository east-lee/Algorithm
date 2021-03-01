T = int(input())
for t in range(1,T+1):
    n = int(input())
    arr = list(list(map(int,input().split())) for _ in range(n))
    # 1은 사람 2는 탈출구
    people = []
    elevator = []
    check = [0 for _ in range(n*n)]

    for i in range(n):
        for j in range(n):
            if arr[i][j] == 1:
                people.append([i,j])
            elif arr[i][j] == 2:
                elevator.append([i,j])


    time_people = [0]*len(people)
    exit_people = [0] * len(people)

    for i in range(len(people)):
        append_list = []
        for j in range(2):
            a,b,c,d = people[i][0],people[i][1],elevator[j][0],elevator[j][1]
            time = abs(a-c)+abs(b-d)
            append_list.append(time)
        time_people[i] = append_list
    print(time_people)
    exit1_stay = []
    exit2_stay = []

    cnt = 0
    while True:
        print(exit1_stay,exit2_stay,exit_people)
        if exit1_stay and exit2_stay and exit2_stay[0] == exit1_stay[0]:
            if len(exit1_stay)> len(exit2_stay):
                exit1_stay.pop(0)
            else:
                exit2_stay.pop(0)
        if exit1_stay:
            for idx,i in enumerate(exit1_stay):
                if exit_people[i] ==0:
                    exit_people[i] = 1
                    exit1_stay.pop(idx)
                    break
        if exit2_stay:
            for idx,i in enumerate(exit2_stay):
                if exit_people[i] == 0:
                    exit_people[i] = 1
                    exit2_stay.pop(idx)
                    break
        for idx,i in enumerate(time_people):
            time1, time2 = i
            if cnt == time1:
                exit1_stay.append(idx)
            if cnt == time2:
                exit2_stay.append(idx)

        if exit_people == [1] * len(people):
            break
        cnt += 1
    print(f'#{t} {cnt}')




