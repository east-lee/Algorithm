testing = True
while testing:
    n = int(input())
    if not n: break
    arr1 = [i for i in range(1,n+1)]
    arr2=[0]*n
    myself = []
    for i in range(n):
        arr2[i]= int(input())
    for i in range(n):
        if arr1[i]==arr2[i]:
            myself.append(i+1)
    max_cnt = 0

    for i in range(n):
        cnt = 0
        total_list = []
        if i+1 not in myself:
            q = []
            while q:
