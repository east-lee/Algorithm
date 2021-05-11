testing = True
while testing:
    input_data =input()
    if not input_data:
        break
    day, num = map(int,input_data.split())
    days_arr = [[1,0],[0,1]]
    if day > 2:
        n = 2
        while n <= day:
            A = days_arr[n-1][0]+days_arr[n-2][0]
            B = days_arr[n - 1][1] + days_arr[n - 2][1]
            days_arr.append([A,B])
            n += 1
    y, x = days_arr[-2][0], days_arr[-2][1]
    A,B=0,0
    for i in range(1,num//y+1):
        num1 = i*y
        if not (num-num1)%x and (num-num1)//x>num1:
            A = i
            B = (num-num1)//x
            print(A)
            print(B)




