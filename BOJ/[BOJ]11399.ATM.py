# 그리디 알고리즘
n = int(input())
arr = list(map(int,input().split()))
arr.sort() 
result = [0]

for i in arr:
    result.append(i+result[-1])

print(sum(result))