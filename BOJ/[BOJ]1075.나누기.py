if __name__ =="__main__":
  N = list(input())[:-2]
  F = int(input())

  for i in range(100):
    if i < 10:
      i = '0'+str(i)
    new_N = int(''.join(N) + str(i))
    if new_N % F == 0:
      print(i)
      break
