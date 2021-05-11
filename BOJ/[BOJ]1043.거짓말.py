from copy import deepcopy

def dfs(k,n,party,know_people,cnt):
  global result
  if k == n:
    if result < cnt: result = cnt
    return

  # 한명이라도 진실을 안다면 무조건 진실만 말해야한다
  know_true_cnt = 0 #진실을 알고있는사람
  know_false_cnt = 0 #거짓을 진실이라고 생각하고 있는 사람
  know_nothing_cnt = 0 #아무것도 모르는 사람람
  tell_true_arr = deepcopy(know_people)
  tell_false_arr =deepcopy(know_people)
  for i in party[k]:
    if know_people[i] == 'knowTrue':
      know_true_cnt +=1
    elif know_people[i] == 'knowFalse': know_false_cnt += 1
    else: know_nothing_cnt += 1
    tell_true_arr[i] = 'knowTrue'
    tell_false_arr[i] = 'knowFalse'


  if know_true_cnt and know_false_cnt: return
  elif know_true_cnt: #진실만을 말해야함
    dfs(k+1,n,party,tell_true_arr,cnt)
  elif know_false_cnt:
    dfs(k+1,n,party,tell_false_arr,cnt+1)
  else: #진실도는 거짓 다말해도됨
    dfs(k+1,n,party,tell_true_arr,cnt)
    dfs(k + 1, n, party, tell_false_arr, cnt + 1)

def main():
  dfs(1,M+1,party,know_people,0)

if __name__ == "__main__":
  N, M = map(int,input().split()) #N = 사람수 // M = 파티의 수
  know_people = [0]*(N+1)
  party = [[] for _ in range(M+1)]
  know_arr = list(map(int,input().split()))

  for i in know_arr[1:]: know_people[i] = 'knowTrue'
  for i in range(1,M+1):
    arr = list(map(int,input().split()))
    party[i] = arr[1:]

  result = 0

  if know_arr[0] == 0:
    print(M)
  else:
    main()
    print(result)



