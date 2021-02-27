# 300000개 테스트케이스..?


T = int(input())
for t in range(1,T+1):
    p,q,r = map(int,input().split())
    a,b,c,d = map(int,input().split())

    circle_point = []
    rectangular_point = []

    circle_point = [[p,q+r],[p,q-r],[p-r,q],[p+r,q]]
    rectangular_point = [[a,b],[c,b],[a,d],[c,d]]

    circle_check = ''
    rectangular_check = ''
    circle_cnt = 0
    rectangular_cnt = 0


    for i in circle_point:
        x,y = i
        if a<=x<=c and b<=y<=d:
            circle_cnt +=1
    for i in rectangular_point:
        x,y = i
        if  (x-p)**2 + (y-q)**2 <= r**2:
            rectangular_cnt+=1
    if circle_cnt == 4:
        circle_check ='N'
    else:
        circle_check='Y'
    if rectangular_cnt==4: rectangular_check='N'
    else: rectangular_check='Y'
    result = circle_check+rectangular_check
    print(f'#{t} {result}')