# 1동 2 서 3 남 4 북
for _ in range(10):
    n = int(input())
    arr = list(list(map(int,input().split())) for _ in range(6))
    height = []
    width = []