# 시간초과

def main():
  p,n = list(input() for _ in range(2))
  arr = list(input().lstrip('[').rstrip(']').split(','))
  # if int(n) >=1:
  #   make_num = ''
  #   for i in input_arr:
  #     if i == '[' or i == ']':continue
  #     if i == ',':
  #       arr.append(int(make_num))
  #       make_num = ''
  #     else: make_num += i
  #   arr.append(int(make_num))
  if int(n) == 0: arr=[]
  reverse_cnt = 0

  for i in p:
    if i == 'R': reverse_cnt += 1
    else:
      # print(arr)
      if not arr: return 'error'
      if reverse_cnt % 2:
        arr.pop()
      else: arr.pop(0)
  if reverse_cnt % 2: arr=arr[::-1]
  for i in range(len(arr)): arr[i] = int(arr[i])
  return arr


if __name__ == "__main__":
  for _ in range(int(input())):
    result = main()
    if result == 'error': print(result)
    else:
      print('[',end='')
      for idx,i in enumerate(result):
        if idx == len(result)-1: print(i,end='')
        else:
          print(i,end='')
          print(',',end='')
      print(']')

