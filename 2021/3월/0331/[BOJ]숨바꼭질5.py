# T = int(input())
# for t in range(1,T+1):
N, K = map(int,input().split())
cnt,subin,result = 1,[N],0

while True:
  if K == N: break
  K += cnt
  if K > 500000:
    result = -1
    break
  new_subin = []
  for i in subin:
    if i+1 <= 500000:
      new_subin.append(i+1)
    if i - 1>=0: new_subin.append(i-1)
    if i*2 <=500000: new_subin.append(i*2)


  if K in new_subin:
    result = cnt
    break

  cnt += 1
  subin= new_subin
print(f'{result}')