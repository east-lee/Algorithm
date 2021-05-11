def main():
  global part,result
  visited = [0]*N
  part.sort(key=lambda x:(x[1]-x[0]),reverse=True)
  sorted_by_start = sorted(part,key=lambda x:x[0])

  for start,end,idx in part:
    cnt = 0
    if visited[idx]: continue
    visited[idx] = 1
    for s,e,index in sorted_by_start:
      if s < start: continue
      elif s >= end: break
      elif s>=start and e<end:
        visited[index] = 1
        cnt += 1
    if result < cnt: result =cnt

if __name__ == "__main__":
  N = int(input())
  part = []
  result = 0
  for i in range(N):
    start,end = map(int,input().split())
    part.append([start,end,i])
  main()
  print(result)