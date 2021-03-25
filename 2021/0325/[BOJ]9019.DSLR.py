# D => (2*n)%10000
# S => n-1 if n != 0 else 9999
# L => d1 d2 d3 d4  > d2 d3 d4 d1
# R => d1 d2 d3 d4 > d4 d1 d2 d3


def main(a,b,result):
  global print_result
  q = [[a,result]]
  new_q = []
  while q:
    x,new_result = q.pop()
    if x == b:
      print_result = new_result
      break
    if x<10000 and check[x] == 0:
      check[x] = 1
      for k in range(4):
        new_x = solution(x,k)
        if check[new_x]: continue
        new_q.append([new_x,new_result+direction[k]])
    if not q and new_q:
      q = new_q
      new_q = []

def solution(x,i):
  if i == 0: return (x*2)%10000
  elif i == 1: return x-1 if x != 0 else 9999
  elif i == 2:
    str_x = str(x)
    for _ in range(4-len(str_x)):
      str_x = '0'+str_x
    str_x = int(str_x[1:] + str_x[:1])
    return str_x
  elif i == 3:
    str_x = str(x)
    for _ in range(4-len(str_x)):
      str_x = '0'+str_x
    str_x = int(str_x[-1:]+str_x[0:-1])
    return str_x


direction = ['D','S','L','R']
if __name__ == "__main__":
  T = int(input())
  for _ in range(T):
    check = [0]*10000
    A, B = map(int,input().split())
    print_result = ''
    main(A,B,'')
    print(print_result)
