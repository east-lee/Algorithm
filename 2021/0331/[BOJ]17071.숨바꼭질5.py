def solution(time_odd,time_even):
  global K
  result_list = []
  cnt = 0
  while K+cnt <= 500000:
    K += cnt
    if time_odd[K] >=0 and time_odd[K] <= cnt and (K-cnt)%2 == 1:
      result_list.append(cnt)
    if time_even[K] >= 0 and time_even[K] <= cnt and (K-cnt)%2 == 0:
      result_list.append(cnt)
    cnt +=1

  if result_list:
    print(min(result_list))
  else:
    print(-1)

def main():
  time_odd = [-1] * 500001
  time_even = [-1] * 500001

  q, new_q = [], []
  q.append(N)
  time_odd[N], time_even[N] = 0,0
  time = 1
  while q:
    x = q.pop()
    check_x = [x-1,x+1,x*2]
    for i in check_x:
      if time % 2 == 0: #짝수일때
        if 0<=i<=500000 and time_even[i] == -1:
          time_even[i] = time
          new_q.append(i)
      else:
        if 0<=i<=500000 and time_odd[i] == -1:
          time_odd[i] = time
          new_q.append(i)

    if not q and new_q:
      q = new_q
      new_q = []
      time += 1
  solution(time_odd,time_even)



if __name__ == "__main__":
  N,K = map(int,input().split())
  main()