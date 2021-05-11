#그리드 알고리즘

n, k = map(int,input().split())
arr = []
for _ in range(n):
    arr.append(int(input()))
arr = arr[::-1]

result = 0 
for i in arr:
    cnt = 0
    if k-i<0:
        continue
    else:
        cnt = k//i
        k = k%i
        result += cnt
    if not k:
        break
print(result)