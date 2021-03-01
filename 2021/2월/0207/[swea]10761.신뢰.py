T = int(input())
for t in range(1,T+1):
    arr = list(map(str,input().split()))
    n = arr[0]
    arr = arr[1:]

    location_ob = [1,1]
    time_ob = [0,0]
    time = 0

    for i in range(int(n)):
        a,b = arr[2*i],int(arr[2*i+1])
        if a == 'O': a = 0
        else : a = 1

        if abs(location_ob[a] - b)<=(time-time_ob[a]):
            time += 1
            location_ob[a] = b
            time_ob[a] = time
        else:
            time += abs(location_ob[a]-b) - (time-time_ob[a]) +1
            location_ob[a] = b
            time_ob[a] = time
    print(f'#{t} {time}')

