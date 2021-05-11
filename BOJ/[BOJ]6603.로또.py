def main(input_data):
  k,s = input_data[0], input_data[1:]
  s.sort()
  dfs(k,s,0,[],-1)
  print()

def dfs(k,s,n,result,last_idx):
  if n == 6:
    for i in result: print(i,end=' ')
    print()
    return

  for i in range(last_idx+1,len(s)):
    dfs(k,s,n+1,result+[s[i]],i)

if __name__ == "__main__":
    while True:
      input_data = list(map(int,input().split()))
      if input_data == [0]: break
      main(input_data)