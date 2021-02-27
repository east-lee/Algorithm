def f(k,result_list):
    global total_list,checking,check_cnt
    if len(result_list)==end:
      ll = result_list[:]
      ll.sort()
      if ll not in total_list:
        total_list.append(ll)
        check_cnt += 1
      if result_list == arr:
        checking = len(total_list)-1
      return
    elif k==n: return
    r = result_list[:]
    rr = result_list[:]
    r.append(k+1)
    f(k+1,r)
    f(k+1,rr)



testing = True
while testing:
    data = input()
    if not data: break
    n,end = map(int,data.split())
    arr = list(map(int,input().split()))
    arr.sort()
    total_list = []
    checking = 0
    check_cnt = 0
    f(0,[])
    try:
      kk = total_list[checking+1]
      for i in kk:
        print(i,end=' ')
      print()

    except:
      print('NONE')