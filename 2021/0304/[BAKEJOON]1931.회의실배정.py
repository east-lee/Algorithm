n = int(input())

conference_time = []
result = 0

for _ in range(n):
    start_time, end_time = map(int,input().split())
    conference_time.append([start_time,end_time])    

conference_time.sort(key= lambda x:(x[1],x[0]))

last_time = -1
for i in conference_time:
    start_time,end_time = i
    if last_time <= start_time:
        last_time = end_time
        result += 1
    else:
        continue
print(result)

