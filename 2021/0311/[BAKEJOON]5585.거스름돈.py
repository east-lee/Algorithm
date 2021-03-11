x = 1000 - int(input())
arr = [500,100,50,10,5,1]
result = 0
for i in arr:
    result += x//i
    x = x%i
print(result)