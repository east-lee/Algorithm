def main(pos_num):
  check_result = True
  for check_num in check:
    strike = 0
    ball = 0
    for i in range(3):
      num = pos_num[i]
      if str(check_num[0])[i] == str(num):
        strike += 1
      elif str(num) in str(check_num[0]):
        ball += 1
    if strike != check_num[1] or ball != check_num[2]:
      check_result = False
      break
  if check_result:return 1
  else: return 0

def find_pos_num(k=0,result = ''):
  global pos_num_list
  if k == 3:
    pos_num_list.append(result)

  for i in range(1,10):
    if str(i) in result: continue
    find_pos_num(k+1,result+str(i))


if __name__ == "__main__":
  N = int(input())
  check = []
  pos_num_list = []
  result = 0

  for _ in range(N):
    check.append(list(map(int,input().split())))
  find_pos_num()

  for pos_num in pos_num_list:
    result += main(pos_num)
  print(result)