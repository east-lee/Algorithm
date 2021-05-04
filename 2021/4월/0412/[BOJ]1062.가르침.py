def solution():
  global result
  alphabet = 'abcdefghijklmnopqrstuvwxyz'
  check = [0]*len(alphabet)
  for i in [0,2,8,13,19]: check[i] = 1
  dfs(0,K-5,check[:],-1)

  for pos in poss_list:
    cnt = 0
    for word in words:
      breaker = False
      for d in word:
        if pos[ord(d)-97] == 1:
          continue
        else:
          breaker = True
          break
      if not breaker: cnt += 1
    if result < cnt:
      result = cnt

def dfs(k,n,new_list,last_idx):
  global poss_list
  if k==n:
    poss_list.append(new_list)
    return
  for i in range(26):
    if i>last_idx and new_list[i] == 0:
      copy_new_list = new_list[:]
      copy_new_list[i] = 1
      dfs(k+1,n,copy_new_list,i)


poss_list = []

if __name__ == "__main__":
  N, K = map(int,input().split())
  words = []
  for _ in range(N):
    word = input()[:-4]
    words.append(list(set(word[4:])))
  result = 0
  if K <5:
    print(0)
  else:
    solution()
    print(result)