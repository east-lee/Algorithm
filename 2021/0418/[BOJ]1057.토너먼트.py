if __name__ == "__main__":
  N,A,B = map(int,input().split())
  cnt = 1
  while True:
    if abs(B-A) == 1 and (A//2 != B//2):
      break
    cnt += 1
    if A%2: A=A//2 + 1
    else: A = A//2
    if B%2: B=B//2 + 1
    else: B=B//2


  print(cnt)




