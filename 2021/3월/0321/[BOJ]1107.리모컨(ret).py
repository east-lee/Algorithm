N = int(input())
M = int(input())
check = [0]*(500000*2+1)
cant = []
if M >= 1:
    cant = list(map(str,input().split()))

min_result = abs(100-N)

q = [N]
new_q = []

while q:
    p = q.pop()
    check[p] = 1
    breaker = True
    for i in str(p):
        if i in cant:
            breaker = False
            break
    if breaker:
        break

    if p+1<(500000*2+1) and check[p+1] == 0:
        new_q.append(p+1)
    if p-1 >=0 and check[p-1] == 0:
        new_q.append(p-1)

    if not q and new_q:
        q = new_q
        new_q = []
print(min(min_result, len(str(p)) + abs(N-p)))
