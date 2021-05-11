f,s,g,u,d = map(int,input().split())
message = "use the stairs"
result = [message]*(f+1)

result[s] = 1

q = [s]
new_q = []

while q:
  point = q.pop()

  if 1<=point-d and result[point-d] == message:
    result[point-d] = result[point] + 1
    new_q.append(point-d)
  if point+u <=f and result[point+u] == message:
    result[point+u] = result[point] + 1
    new_q.append(point + u)

  if not q and new_q:
    q = new_q
    new_q = []
if result[g] == message: print(message)
else: print(result[g] -1)
