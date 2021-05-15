def main():
  cnt = 0
  for i in range(len(L)):
    if L[i] != R[i]: break
    elif L[i] == '8':  cnt += 1
  print(cnt)

if __name__ == "__main__":
  L, R = map(str,input().split())
  if len(L) < len(R):    print(0)
  else: main()