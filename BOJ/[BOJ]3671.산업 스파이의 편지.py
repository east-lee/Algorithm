def DFS(k,N,result):
  global set_prime, check_list
  if result and prime[int(result)] == True:
    set_prime.add(int(result))
  if k == N:
    return

  for i in range(N):
    if check_list[i] == 1: continue
    check_list[i] = 1
    DFS(k+1,N,result+str(num_list[i]))
    check_list[i] = 0


def Eratosthenes():
  max_size = 10**7
  prime = [True] * max_size

  prime[0], prime[1] = False, False

  for i in range(2,max_size):
    if prime[i]:
      x = i + i
      while x < max_size:
        prime[x] = False
        x += i

  return prime

if __name__ == "__main__":
  TC = int(input())
  prime = Eratosthenes()
  for _ in range(TC):
    num_list = list(map(int,list(input())))
    check_list = [False] * len(num_list)
    set_prime = set()
    DFS(0,len(num_list),'')
    print(len(set_prime))