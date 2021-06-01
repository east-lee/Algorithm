def change_status(num):
  global switch_status
  switch_status[num] = 1 if switch_status[num] == 0 else 0


def man_switch(num):
  cnt = num
  while cnt <= N:
    change_status(cnt)
    cnt += num


def woman_switch(num):
  global switch_status
  change_list = [num]
  cnt = 0
  while True:
    cnt += 1
    left, right = num-cnt, num+cnt
    if left <=0 or right > N: break
    if switch_status[left] != switch_status[right]:
      break
    change_list.extend([left,right])

  for i in change_list: change_status(i)


if __name__ == "__main__":
  N = int(input())
  switch_status = list(map(int,input().split()))
  switch_status.insert(0,0)

  loop_cnt = int(input())

  for _ in range(loop_cnt):
    gender, switch_num = map(int,input().split())
    if gender == 1: man_switch(switch_num)
    else: woman_switch(switch_num)
    
  for i in range(1,N+1):
    if i > 1 and i % 20 == 0:
      print(switch_status[i])
    else:
      print(switch_status[i],end=' ')